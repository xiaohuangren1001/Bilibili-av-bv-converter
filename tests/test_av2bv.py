import unittest
from abv_py import av2bv


class Av2bvTest(unittest.TestCase):
    def test_avid_too_small(self):
        self.assertRaises(TypeError, lambda: av2bv(0))

    def test_avid_too_big(self):
        self.assertRaises(TypeError, lambda: av2bv(1 + (1 << 51)))

    def test_avid_convert(self):
        self.assertEqual(av2bv(11451419180), "BV1gA4v1m7BV")
        self.assertEqual(av2bv(170001), "BV17x411w7KC")
