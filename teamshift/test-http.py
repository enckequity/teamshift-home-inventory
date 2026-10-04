"""Disposable local HTTP acceptance; never run against a real household database."""
import json,secrets,urllib.request,urllib.error,urllib.parse,uuid,datetime,csv,io
from PIL import Image
import zxingcpp
BASE='http://127.0.0.1:8770/api/v1'
def req(method,path,body=None,token=None,tenant=None,raw=None,ctype=None):
 headers={}
 if token:headers['Authorization']=token
 if tenant:headers['X-Tenant']=tenant
 data=raw
 if body is not None:data=json.dumps(body).encode();headers['Content-Type']='application/json'
 if ctype:headers['Content-Type']=ctype
 try:
  with urllib.request.urlopen(urllib.request.Request(BASE+path,data=data,headers=headers,method=method),timeout=30) as r:code=r.status;data=r.read()
 except urllib.error.HTTPError as e:code=e.code;data=e.read()
 try:parsed=json.loads(data)
 except (json.JSONDecodeError,UnicodeDecodeError):parsed=None
 return code,parsed,data

def success(result,label):
 assert 200<=result[0]<300,(label,result[0]);return result[1]
def register(label,invite=None):
 email='fixture-'+label+'-'+uuid.uuid4().hex[:10]+'@example.invalid';password=secrets.token_urlsafe(24)
 b=dict(name='TEST ONLY '+label,email=email,password=password)
 if invite:b['token']=invite
 success(req('POST','/users/register',b),'register '+label)
 login=success(req('POST','/users/login',dict(username=email,password=password,stayLoggedIn=False)),'login '+label)
 return login['token']
def entities(value):
 if isinstance(value,list):return value
 if isinstance(value,dict):
  for key in ['items','data','entities']:
   if isinstance(value.get(key),list):return value[key]
 raise AssertionError('Unrecognized entity list shape')

a=register('owner-a');b=register('owner-b')
ga=success(req('POST','/groups',dict(name='TEST ONLY household A shared'),a),'create A')['id']
gb=success(req('POST','/groups',dict(name='TEST ONLY household B'),b),'create B')['id']
def types(token,group):
 ts=success(req('GET','/entity-types',token=token,tenant=group),'types')
 ts=entities(ts) if not isinstance(ts,list) else ts
 return next(t['id'] for t in ts if t.get('isLocation')),next(t['id'] for t in ts if not t.get('isLocation'))
la,ia=types(a,ga);lb,ib=types(b,gb)
closet=success(req('POST','/entities',dict(name='TEST ONLY closet A',quantity=1,entityTypeId=la),a,ga),'create closet')
marker='TEST ONLY private A marker '+uuid.uuid4().hex
bin1=success(req('POST','/entities',dict(name='B001 fixture bin',quantity=1,parentId=closet['id'],entityTypeId=ia,description=marker),a,ga),'create bin')
qr_target='http://127.0.0.1:8770/item/'+bin1['id']
qr= req('GET','/qrcode?data='+urllib.parse.quote(qr_target,safe=''),token=a,tenant=ga)
assert qr[0]==200 and qr[2].startswith(b'\xff\xd8'),('QR generation',qr[0])
decoded=zxingcpp.read_barcode(Image.open(io.BytesIO(qr[2])))
assert decoded is not None and decoded.text==qr_target,'Native QR must decode to stable entity URL without credentials'
expiry=(datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=1)).isoformat()
invite=success(req('POST','/groups/invitations',dict(uses=1,expiresAt=expiry),a,ga),'invite')
member=register('member-a',invite['token'])
read=success(req('GET','/entities/'+bin1['id'],token=member,tenant=ga),'member shared read');assert read['description']==marker
success(req('PATCH','/entities/'+bin1['id'],dict(quantity=2),member,ga),'member content write')
for path in ['/entities','/groups','/entities/'+bin1['id']]:
 result=req('GET',path,token=b,tenant=ga);assert result[0]==403 and marker.encode() not in result[2],('foreign selector',result[0])
assert req('GET','/entities',token=b,tenant=str(uuid.uuid4()))[0]==403
for method,payload in [('GET',None),('PUT',dict(name='ATTEMPTED FOREIGN WRITE',quantity=999,entityTypeId=ib)),('PATCH',dict(quantity=999))]:
 result=req(method,'/entities/'+bin1['id'],payload,b,gb);assert result[0] in (403,404) and marker.encode() not in result[2],('foreign object',method,result[0])
for payload in [dict(name='invalid parent',quantity=1,parentId=closet['id'],entityTypeId=ib),dict(name='invalid type',quantity=1,entityTypeId=ia)]:assert req('POST','/entities',payload,b,gb)[0] in (400,403,404)
read=success(req('GET','/entities/'+bin1['id'],token=a,tenant=ga),'owner readback');assert read['quantity']==2 and read['description']==marker
for method,path,payload in [('PUT','/groups',dict(name='Unauthorized rename',currency='USD')),('POST','/groups/invitations',dict(uses=1,expiresAt=expiry)),('DELETE','/groups',None)]:assert req(method,path,payload,member,ga)[0]==403,('member admin',method,path)
success(req('PUT','/groups',dict(name='TEST ONLY verified household A',currency='USD'),a,ga),'owner administration')
assert req('GET','/entities/'+bin1['id'])[0] in (401,403)
# Session query auth must be refused. Do not emit the URL or token in logs.
assert req('GET','/entities/'+bin1['id']+'?access_token='+urllib.parse.quote(a.removeprefix('Bearer ')))[0] in (401,403)
imported_id=None
for description in ['TEST ONLY imported bin','TEST ONLY updated bin contents']:
 text='HB.import_ref,HB.name,HB.location,HB.quantity,HB.description,HB.field.bin_id\nfixture-bin-B002,B002 fixture bin,Fixture Apartment / Primary closet,1,'+description+',B002\n'
 boundary='fixture-'+uuid.uuid4().hex
 raw=(f'--{boundary}\r\nContent-Disposition: form-data; name="csv"; filename="fixture.csv"\r\nContent-Type: text/csv\r\n\r\n'+text+f'\r\n--{boundary}--\r\n').encode()
 success(req('POST','/entities/import',token=a,tenant=ga,raw=raw,ctype='multipart/form-data; boundary='+boundary),'CSV import')
 listed=success(req('GET','/entities?limit=100',token=a,tenant=ga),'list after import');items=entities(listed)
 matches=[x for x in items if x.get('name')=='B002 fixture bin'];assert len(matches)==1,'CSV duplicate'
 current=success(req('GET','/entities/'+matches[0]['id'],token=a,tenant=ga),'imported bin readback')
 assert current['description']==description,'Import must update actual contents'
 if imported_id is not None:assert current['id']==imported_id,'Import must retain immutable item URL'
 imported_id=current['id']
other=success(req('GET','/entities?limit=100',token=b,tenant=gb),'B listing');assert 'B002 fixture bin' not in json.dumps(other) and marker not in json.dumps(other)
print('PASS: two-household membership/object isolation; invited content access; member-admin refusal; owner positive; auth/query refusal; native QR decoding; CSV update without duplicate or changed item ID')
