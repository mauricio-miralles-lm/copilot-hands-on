import unittest
from prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        # Test cases for non-prime numbers
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(121))
        
        # Test cases for prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(37))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(43))
        self.assertTrue(is_prime(47))
        self.assertTrue(is_prime(53))
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(997))

if __name__ == '__main__':
    unittest.main()
