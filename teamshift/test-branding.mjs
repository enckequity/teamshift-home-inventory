import assert from 'node:assert/strict';import {readFileSync,readdirSync} from 'node:fs';import {brandMessage,buildSourceUrl} from '../frontend/lib/brand.ts';
assert.equal(brandMessage('Welcome to HomeBox.'), 'Welcome to TeamShift.');assert.equal(brandMessage('Homebox-asennukseen.'), 'TeamShift-asennukseen.');assert.equal(brandMessage('homebox-frontend'), 'homebox-frontend');assert.equal(brandMessage('homebox_entities'), 'homebox_entities');assert.equal(brandMessage('https://HomeBox.software/en/'), 'https://HomeBox.software/en/');assert.equal(brandMessage('HomeBox inventory'), 'TeamShift inventory');assert.equal(brandMessage('Homebox label'), 'TeamShift label');assert.equal(brandMessage('homebox inventory'), 'TeamShift inventory');assert.equal(brandMessage('https://homebox.software/en/api/'), 'https://homebox.software/en/api/');assert.equal(brandMessage('https://github.com/sysadminsmedia/homebox'), 'https://github.com/sysadminsmedia/homebox');assert.equal(brandMessage('HB.import_ref {username}'), 'HB.import_ref {username}');assert.match(readFileSync('frontend/nuxt.config.ts','utf8'),/name: "TeamShift Home Inventory"/);assert.match(readFileSync('frontend/components/App/Logo.vue','utf8'),/aria-label="TeamShift"/);assert.match(readFileSync('frontend/pages/index.vue','utf8'),/github.com\/enckequity\/teamshift-home-inventory/);assert(!readFileSync('frontend/pages/index.vue','utf8').includes('HomeB\n'));
const walk=p=>readdirSync(p,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(p+'/'+e.name):[p+'/'+e.name]);for(const path of walk('frontend/pages').filter(p=>p.endsWith('.vue'))){const s=readFileSync(path,'utf8');assert(!/title:.*["`]Home[Bb]ox/.test(s),path);assert(!/<h1>HomeBox/.test(s),path)}
assert.match(readFileSync('frontend/lib/data/themes.ts','utf8'),/label: "TeamShift"/);
console.log('PASS: TeamShift UI titles/logo/manifest; human translations; URL/technical ID preservation; modified source link');

const header = readFileSync('frontend/components/App/HeaderText.vue', 'utf8');
assert.match(header, /aria-label="TeamShift"/);
assert.match(header, />TeamShift<\/span>/);
assert(!header.includes('<path'), 'authenticated wordmark must not retain upstream SVG paths');
const logo = readFileSync('frontend/components/App/Logo.vue', 'utf8');
assert.match(logo, /<rect width="64" height="64" rx="14"/);
const layout = readFileSync('frontend/layouts/default.vue', 'utf8');
assert.match(layout, /buildSourceUrl\(status.value\?\.build.commit/);
assert.match(layout, /global.footer.upstream_api_docs/);
assert(!layout.includes('global.footer.version_link'));
assert(!layout.includes('global.footer.api_link'));
assert(!layout.includes('OutdatedModal'), 'upstream update notices must not advertise TeamShift upgrades');
const login = readFileSync('frontend/pages/index.vue', 'utf8');
assert(!login.includes('noc.social'));
assert(!login.includes('discord.gg'));
assert.match(login, /global.footer.upstream_docs/);
const source = 'https://github.com/enckequity/teamshift-home-inventory';
assert.equal(buildSourceUrl('6b3727cd'), source + '/commit/6b3727cd');
assert.equal(buildSourceUrl('a'.repeat(40)), source + '/commit/' + 'a'.repeat(40));
for (const invalid of ['', 'dev', 'https://evil.example', '../main', 'a'.repeat(41)]) assert.equal(buildSourceUrl(invalid), source);
console.log('PASS: authenticated TeamShift wordmark, usable logo, deployed-build source, explicit upstream help, no upstream social/update channels');
