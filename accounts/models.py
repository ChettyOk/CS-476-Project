from django.db import models
import re

class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=200)
    course_faculty = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

    @staticmethod
    def check_course_code_spelling(course_code):
        if not course_code or not isinstance(course_code, str):
            return False
        course_code = course_code.strip().upper()
        pattern = r"^[A-Z]{2,4}\s?\d{3}$"
        return bool(re.match(pattern, course_code))

    @classmethod
    def createCourse(cls, course_code, course_name, course_faculty):

        if not cls.check_course_code_spelling(course_code):
            raise ValueError(f'invalid course code')

        course_code = course_code.strip().upper()
        
        return cls.objects.create(course_code = course_code, course_name = course_name, course_faculty = course_faculty)
        
            

        
        


# User
#     ID
#     first, last name
#     email
#     password -> Hash
#     phone number ?
#     role
#     created at
#     updated at
#     max Time session ?
#     set Password()
#     check Password()
#     has Role()
#     Switch Role()
#     update Contact Data()
#     change Password()
#     check Email()
#     delete profil()
#     log out idle time()

# StudentProfil
#     User ID
#     StudentProfil ID
#     major
#     courses
#     semester
#     is Tutor
#     average rating
#     add Course()
#     remove Course()
#     update Profil()
#     add favorite Tutor()
#     get Enrolled Courses()

# TutorProfil
#     User ID
#     Tutor Profil ID
#     courses passed
#     average Rating
#     (bio)
#     calculate Rating()

# Courses
#     ID
#     course code
#     course name
#     faculty
#     (description)
#     create Course()
#     update Course()
#     (get Courses from file())
#     (get Courses from API())
#     (check Course Code spelling())