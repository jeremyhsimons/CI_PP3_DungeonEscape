import unittest
import validation


class TestValidate(unittest.TestCase):

    def test_validate_yes_no(self):
        """
        Tests if validate_yes_no function returns expected values.
        """
        result = validation.validate_yes_no("y")
        self.assertEqual(result, True)


# code below from Corey Schafer
if __name__ == '__main__':
    unittest.main()
