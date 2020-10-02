import unittest
import main

main = main


class TestClass(unittest.TestCase):
    def test_00_exists(self):
        self.assertTrue(True)

    def test_01_main_exists(self):
        self.assertIsNotNone(main)

    def test_02_dictionary_exists(self):
        dictionary = main.decryption_dictionary
        print(dictionary)
        self.assertIsNotNone(dictionary)

    def test_03_user_input_received(self):
        main.user_selection()

    def test_04_dictionary_lists_exist(self):
        key_list = main.dictionary_keys
        value_list = main.dictionary_values
        self.assertIsNotNone(key_list)
        self.assertIsNotNone(value_list)

    def test_05_encrypt_message(self):
        # string = main.user_selection
        pass
