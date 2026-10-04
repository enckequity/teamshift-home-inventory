import assert from 'node:assert/strict';
import { labelDestination } from '../frontend/lib/label-destination.ts';
const id='52af921e-f093-48dc-aeda-f94d631074ab';
assert.equal(labelDestination(' https://inventory.example/ ', '000-001', id), 'https://inventory.example/item/'+id);
assert.equal(labelDestination('https://inventory.example', '000-002', id), 'https://inventory.example/item/'+id);
assert.equal(labelDestination('https://inventory.example/', '000-001'), 'https://inventory.example/a/000-001');
console.log('PASS: real labels retain immutable item URLs when asset display IDs change; blank labels retain native asset lookup');
