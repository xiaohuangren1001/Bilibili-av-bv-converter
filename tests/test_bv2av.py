import unittest
from abv_py import bv2av


class Bv2avTest(unittest.TestCase):
    def test_bvid_convert(self):
        self.assertEqual(bv2av("BV1B8Ziyo7s2"), 1145141919810)

    def test_bvid_prefix(self):
        self.assertRaises(TypeError, lambda: bv2av(""))
        self.assertRaises(TypeError, lambda: bv2av("    "))
        self.assertRaises(TypeError, lambda: bv2av("1B8Ziyo7s2"))

    def test_bvid_non_ascii(self):
        self.assertRaises(TypeError, lambda: bv2av("BV1测试Unicode"))

    def test_bvid_incorrect_length(self):
        self.assertRaises(TypeError, lambda: bv2av("BV11B8Ziyo7s2"))
        self.assertRaises(TypeError, lambda: bv2av("BV18Ziyo7s2"))

    def test_bvid_illegal_character(self):
        illegal_chars = ["0", "O", "I", "l", "+", "/"]
        for ch in illegal_chars:
            self.assertRaises(TypeError, lambda: bv2av(f"BV1{ch}8Ziyo7s2"))


"""
#[test]
fn bv2av_test() {
  assert_eq!(1145141919810, bv2av("").unwrap());

  assert_eq!(bv2av(""), Err(Error::BvEmpty));
  assert_eq!(bv2av("   "), Err(Error::BvTooSmall));
  assert_eq!(bv2av("BV测试"), Err(Error::BvWithUnicode));
  assert_eq!(bv2av("BV2B8Ziyo7s2"), Err(Error::BvInvalidPrefix));
  assert_eq!(bv2av("BV212312"), Err(Error::BvTooSmall));
  assert_eq!(bv2av("BV2122222222312"), Err(Error::BvTooBig));
  assert_eq!(bv2av("BV1B0Ziyo7s2"), Err(Error::BvInvalidChar('0')));
}
"""
