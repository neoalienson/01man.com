const assert = require('assert');
const sinon = require('sinon');
const uuid = require('uuid');
const rewire = require('rewire');

const {marksix} = require('..');
const app = rewire('..');

var range = app.__get__('range');

it('range should generate 49 numbers', () => {
  var r = range(1, 49);
  assert.equal(r.length, 49);
});

it('range should be incremental from 1 to 49 by 1', () => {
  var r = range(1, 49);
  for (var i = 0; i< 49; i++) {
    assert.equal(r[i], i + 1);
  }
});

it('marksix: should be a json object with field lucky_numbers and 6 numbers', () => {
  // Mock ExpressJS 'req' and 'res' parameters
  const name = uuid.v4();
  const req = {
    query: {},
    body: {
      name: name,
    },
  };
  const res = {send: sinon.stub()};

  // Call tested function
  marksix(req, res);

  // Verify behavior of tested function
  assert.ok(res.send.calledOnce);
  r = res.send.firstCall.args;
  assert.ok(r[0].hasOwnProperty('lucky_numbers'), 'lucky_numbers is missing');
  assert.equal(r[0].lucky_numbers.length, 6);
});
