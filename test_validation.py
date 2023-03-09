import unittest
import validation


class TestValidate(unittest.TestCase):

    def test_validate_yes_no(self):
        """
        Tests if validate_yes_no function returns expected values.
        """
        self.assertEqual(validation.validate_yes_no("y"), True)
        self.assertEqual(validation.validate_yes_no("n"), True)
        # Edge cases
        self.assertEqual(validation.validate_yes_no(""), False)
        self.assertEqual(validation.validate_yes_no(" "), False)
        self.assertEqual(validation.validate_yes_no("1"), False)
        self.assertEqual(validation.validate_yes_no("h"), False)
        self.assertEqual(validation.validate_yes_no("Y"), False)
        self.assertEqual(validation.validate_yes_no("nn"), False)

    def test_validate_details(self):
        """
        Tests if validate_details function returns expected values.
        """
        self.assertEqual(validation.validate_details("User123", "Password123"), True)
        # Testing an existing user's details.
        self.assertEqual(validation.validate_details("test_user", "password"), False)
        self.assertEqual(validation.validate_details("User123", " "), False)
        self.assertEqual(validation.validate_details("User123", ""), False)
        self.assertEqual(validation.validate_details(" ", "Password123"), False)
        self.assertEqual(validation.validate_details("", "Password123"), False)


# code below from Corey Schafer
if __name__ == '__main__':
    unittest.main()
