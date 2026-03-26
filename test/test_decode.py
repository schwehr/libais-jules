#!/usr/bin/env python

"""Test the top level decoders with a single message each."""

import ais
import unittest
from . import test_data
import sys

class AisTopLevelDecoders(unittest.TestCase):

  def setUp(self):
    self.maxDiff = None

  def testAll(self):
    """Decode one of each top level message"""
    for entry in test_data.top_level:
      body = ''.join([line.split(',')[5] for line in entry['nmea']])
      pad = int(entry['nmea'][-1].split('*')[0][-1])
      msg = ais.decode(body, pad)
      expected = entry['result']
      if msg.keys() != expected.keys():
        sys.stderr.write('key mismatch: %s\n' % set(msg).symmetric_difference(set(expected)))
      self.assertDictEqual(
          expected, msg,
          'Mismatch for id:%d\n%s\n%s\n  From: %s' % (
              msg['id'], msg, expected, entry['nmea']))


class Ais20Decoders(unittest.TestCase):

  def testDecodeMessage20(self):
    # !AIVDM,1,1,,B,D02E35iqlg6D,0*41
    msg = ais.decode('D02E35iqlg6D', 0)
    expected = {
        'id': 20,
        'mmsi': 2442007,
        'repeat_indicator': 0,
        'reservations': [{'incr': 1125, 'num_slots': 2, 'offset': 1949, 'timeout': 7}],
        'spare': 0
    }
    self.assertDictEqual(expected, msg, "Failed decoding Message 20")

class Ais6Decoders(unittest.TestCase):

  def testDecodeUnknownMessage6(self):
    # !AIVDM,1,1,,B,6B?n;be:cbapalgc;i6?Ow4,2*4A'
    # TODO(schwehr): Expose the C++ Python exception to Python.
    self.assertRaisesRegex(ais.DecodeError, '6:669:11',
                           ais.decode, '6B?n;be:cbapalgc;i6?Ow4', 2)

if __name__=='__main__':
  unittest.main()
