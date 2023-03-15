# Imports
# Python
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import validation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestValidate(unittest.TestCase):
    
    def test_validate_yes_no(self):
        """
        Tests if validate_yes_no function returns expected values.
        """
        self.assertEqual(validation.validate_yes_no("y"), True)
        self.assertEqual(validation.validate_yes_no("n"), True)
        # Edge cases.
        self.assertEqual(validation.validate_yes_no(""), False)
        self.assertEqual(validation.validate_yes_no(" "), False)
        self.assertEqual(validation.validate_yes_no("1"), False)
        self.assertEqual(validation.validate_yes_no("h"), False)
        self.assertEqual(validation.validate_yes_no("Y"), False)
        self.assertEqual(validation.validate_yes_no("nn"), False)
        self.assertEqual(validation.validate_yes_no(0), False)
        self.assertEqual(validation.validate_yes_no(True), False)

    def test_validate_details(self):
        """
        Tests if validate_details function returns expected values.
        """
        # Testing entry for new user -> should return true.
        self.assertEqual(
            validation.validate_details("User123", "Password123"), True
            )
        # Testing an existing user's details -> should return false.
        self.assertEqual(
            validation.validate_details("test_user", "password"), False
            )
        # Edge cases.
        self.assertEqual(validation.validate_details("User123", " "), False)
        self.assertEqual(validation.validate_details("User123", ""), False)
        self.assertEqual(
            validation.validate_details(" ", "Password123"), False
            )
        self.assertEqual(validation.validate_details("", "Password123"), False)
        self.assertEqual(validation.validate_details(0, 0), False)
        self.assertEqual(validation.validate_details(True, True), False)

    def test_validate_main_menu(self):
        """
        Tests if the validate_main_menu function returns expected values.
        """
        self.assertEqual(validation.validate_main_menu("x"), True)
        self.assertEqual(validation.validate_main_menu("s"), True)
        self.assertEqual(validation.validate_main_menu("i"), True)
        # Edge cases.
        self.assertEqual(validation.validate_main_menu("X"), False)
        self.assertEqual(validation.validate_main_menu(" "), False)
        self.assertEqual(validation.validate_main_menu(""), False)
        self.assertEqual(validation.validate_main_menu("1"), False)
        self.assertEqual(validation.validate_main_menu("%"), False)
        self.assertEqual(validation.validate_main_menu(0), False)
        self.assertEqual(validation.validate_main_menu(True), False)

    def test_validate_math(self):
        """
        Tests if the validate_math function returns expected values.
        """
        self.assertEqual(validation.validate_math("1"), True)
        self.assertEqual(validation.validate_math("0"), True)
        self.assertEqual(validation.validate_math("1234567"), True)
        # Edge cases.
        self.assertEqual(validation.validate_math(""), False)
        self.assertEqual(validation.validate_math(" "), False)
        self.assertEqual(validation.validate_math("abc"), False)
        self.assertEqual(validation.validate_math("$"), False)
        self.assertEqual(validation.validate_math(0), False)
        self.assertEqual(validation.validate_math(True), False)

    def test_validate_navigation(self):
        """
        Tests if the validate_navigation function returns expected values.
        """
        self.assertEqual(validation.validate_navigation("U,1"), True)
        self.assertEqual(validation.validate_navigation("D,2"), True)
        self.assertEqual(validation.validate_navigation("R,3"), True)
        self.assertEqual(validation.validate_navigation("L,4"), True)
        # Edge cases.
        self.assertEqual(validation.validate_navigation(""), False)
        self.assertEqual(validation.validate_navigation(" "), False)
        self.assertEqual(validation.validate_navigation("U1"), False)
        self.assertEqual(validation.validate_navigation("U,12"), False)
        self.assertEqual(validation.validate_navigation("d,1"), False)
        self.assertEqual(validation.validate_navigation("1,1"), False)
        self.assertEqual(validation.validate_navigation("1"), False)
        self.assertEqual(validation.validate_navigation("D,D"), False)

    def test_validate_string(self):
        """
        Tests that validate_string returns expected values.
        """
        self.assertEqual(validation.validate_string('abc'), True)
        self.assertEqual(validation.validate_string('123'), True)
        self.assertEqual(validation.validate_string('ab£'), True)
        # Edge cases
        self.assertEqual(validation.validate_string(''), False)
        self.assertEqual(validation.validate_string(' '), False)
        self.assertEqual(validation.validate_string(123), False)
        self.assertEqual(validation.validate_string(True), False)

    def test_validate_message(self):
        """
        Tests that validate_message returns expected values.
        """
        self.assertEqual(validation.validate_message("Hello, world!"), True)
        # Edge cases
        self.assertEqual(validation.validate_message(""), False)
        self.assertEqual(validation.validate_message(" "), False)
        self.assertEqual(validation.validate_message(
            """
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            """
            ), False)


# code below from Corey Schafer
if __name__ == '__main__':
    unittest.main()
