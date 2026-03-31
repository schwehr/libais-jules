import unittest
from ais.stream import checksum

class ChecksumValidTest(unittest.TestCase):

    def test_valid_checksum(self):
        self.assertTrue(checksum.isChecksumValid("!AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0*09"))
        self.assertTrue(checksum.isChecksumValid("AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0*09"))

    def test_invalid_checksum(self):
        self.assertFalse(checksum.isChecksumValid("!AIVDM,11,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0*09"))
        self.assertFalse(checksum.isChecksumValid("!AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0*FF"))

    def test_allow_tail_data(self):
        # When allowTailData=True (default), strings with data after the checksum are valid
        self.assertTrue(checksum.isChecksumValid("!AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0*09,b003669952,1370785759"))

        # When allowTailData=False, such strings fail validation
        self.assertFalse(checksum.isChecksumValid("!AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0*09,b003669952,1370785759", allowTailData=False))

    def test_no_match_allow_tail_data(self):
        # When allowTailData=True but there is no valid nmea checksum pattern
        self.assertFalse(checksum.isChecksumValid("!AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0", allowTailData=True))

    def test_missing_checksum_indicator(self):
        # Without allowTailData, it must have '*' at the 3rd to last character
        self.assertFalse(checksum.isChecksumValid("!AIVDM,1,1,,B,35MsUdPOh8JwI:0HUwquiIFH21>i,0X09", allowTailData=False))

    def test_short_string_index_error(self):
        # The current implementation raises IndexError for strings shorter than 3 chars when allowTailData=False
        with self.assertRaises(IndexError):
            checksum.isChecksumValid("a", allowTailData=False)

if __name__ == '__main__':
    unittest.main()
