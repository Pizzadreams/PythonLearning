import unittest
from password_generator import PasswordGenerator  # Import your PasswordGenerator class

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        generator = PasswordGenerator()
        generated_password = generator.generate_password(5, 10, 4)  # Customize the parameters for your test
        self.assertEqual(len(generated_password), 10)

    def test_generate_password_contains_letters(self):
        generator = PasswordGenerator()
        generated_password = generator.generate_password(10, 3, 5)  # Customize the parameters for your test
        self.assertTrue(any(c.isalpha() for c in generated_password))

    def test_generate_password_contains_symbols(self):
        generator = PasswordGenerator()
        generated_password = generator.generate_password(4, 3, 2)  # Customize the parameters for your test
        self.assertTrue(any(c in "!#$%&()*+" for c in generated_password))

    def test_generate_password_contains_numbers(self):
        generator = PasswordGenerator()
        generated_password = generator.generate_password(12, 42, 561)  # Customize the parameters for your test
        self.assertTrue(any(c.isdigit() for c in generated_password))

if __name__ == '__main__':
    unittest.main()
