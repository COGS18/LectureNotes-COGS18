import unittest
from atbash import atbash_encrypt, atbash_decrypt, atbash_wrapper

class TestEncrypt(unittest.TestCase):
    
    def test_exist(self):
        self.assertTrue(callable(atbash_encrypt))

    def test_type(self):
        self.assertIsInstance(atbash_encrypt('hello'), str)

    def test_output(self):
        self.assertEqual('SVOOL', atbash_encrypt('HELLO'))
        self.assertEqual('SVOOL', atbash_encrypt('hello'))


class TestDecrypt(unittest.TestCase):
    
    def test_exist(self):
        self.assertTrue(callable(atbash_decrypt))

    def test_type(self):
        self.assertIsInstance(atbash_decrypt('hello'), str)

    def test_output(self):
        self.assertEqual('HELLO', atbash_decrypt('SVOOL'))
        self.assertEqual('HELLO', atbash_decrypt('svool'))


class TestWrapper(unittest.TestCase):
    
    def test_exist(self):
        self.assertTrue(callable(atbash_wrapper))

    def test_type(self):
        self.assertIsInstance(atbash_wrapper('hello', method='encrypt'), str)

    def test_output_encrypt(self):
        self.assertEqual('SVOOL', atbash_wrapper('hello', method='encrypt'))
        self.assertEqual('SVOOL', atbash_wrapper('HELLO', method='encrypt'))

    def test_output_decrypt(self):
        self.assertEqual('HELLO', atbash_wrapper('SVOOL', method='decrypt'))
        self.assertEqual('HELLO', atbash_wrapper('svool', method='decrypt'))

    def test_output_other(self):
        self.assertEqual("method should be either 'decrypt' or 'encrypt'", atbash_wrapper('svool', method='blargh'))
