from django.test import TestCase
from .models import Course
from django.db import IntegrityError

class test_course(TestCase):

    def test_course_code_validity(self):
        self.assertTrue(Course.check_course_code_spelling("CS 476"))
        self.assertTrue(Course.check_course_code_spelling("CS476"))
        self.assertTrue(Course.check_course_code_spelling("ENER 476"))
        self.assertTrue(Course.check_course_code_spelling("cs 476"))

        self.assertFalse(Course.check_course_code_spelling("xxx"))
        self.assertFalse(Course.check_course_code_spelling(""))
        self.assertFalse(Course.check_course_code_spelling("CS 47"))
        self.assertFalse(Course.check_course_code_spelling("MATHEMATICS 476"))
        self.assertFalse(Course.check_course_code_spelling("C 476"))

    def test_course_creation(self):  
        course = Course.createCourse("CS 476", "Computer Science 476", "Science")  
        self.assertEqual(course.course_code, "CS 476")
        self.assertEqual(course.course_name, "Computer Science 476")
        self.assertEqual(course.course_faculty, "Science")
        self.assertTrue(Course.objects.filter(course_code='CS 476').exists())  
        
    def test_invalid_course_creation(self):
        with self.assertRaises(ValueError):
            Course.createCourse("xxx", "Computer Science 476", "Science")

    def test_course_duplicate_prevention(self):
        created1 = Course.createCourse("CS 476", "Computer Science 476", "Science")
        self.assertTrue(created1)
        with self.assertRaises(IntegrityError):
            Course.createCourse("CS 476", "Computer Science 476", "Science")
