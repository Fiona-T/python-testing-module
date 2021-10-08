# file must start with the word test
import unittest
# import class to test
from student import Student
# for apply_extension test
from datetime import timedelta
# for mocking a get request
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    # to set up once, before any test is ran
    # class method means it acts on the class instead of instance of class
    @classmethod
    def setUpClass(cls):
        print("set up class")

    # to tear down once, after all tests are ran
    # class method means it acts on the class instead of instance of class
    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    # to run before each test method
    def setUp(self):
        print('set up')
        self.student = Student("John", "Doe")

    # to run after each test method - not needed in this case so just printing
    def tearDown(self):
        print('tear down')

    def test_full_name(self):
        print('test full name')
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print('test alert santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test email')
        # lower case for email address
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        current_end_date = self.student.end_date
        # import timedelta above for this
        test_end_date = current_end_date + timedelta(days=5)
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, test_end_date)
        # alternative instead of using test_end_date above
        # self.assertEqual(self.student.end_date, current_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        # set the context manager, creates object called mocked_get
        with patch("student.requests.get") as mocked_get:
            # set the values for .ok and .get response from api
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            # call the method, store in schedule variable
            schedule = self.student.course_schedule()
            # test that method call returns Success string
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        # set the context manager, creates object called mocked_get
        with patch("student.requests.get") as mocked_get:
            # set the values for .ok response from api
            mocked_get.return_value.ok = False
            # call the method, store in schedule variable
            schedule = self.student.course_schedule()
            # test that method call returns correct string when response is not ok
            self.assertEqual(schedule, "Something went wrong with the request")


if __name__ == "__main__":
    unittest.main()
