# .\venv\Scripts\Activate.ps1
from django.db import models
import re
import json
import os
import pypdf
from .constants import FACULTIES

class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=200)
    course_faculty = models.CharField(max_length=50)

    FACULTIES = FACULTIES

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

    @classmethod
    def getCoursesFromFile(cls, pdf_file):
        file = pypdf.PdfReader(pdf_file)
        name_pattern = re.compile(r'^([A-Z]{2,4}\s\d{3})\s*-\s*(.+)$')
        
        num_of_created = 0
        num_of_skipped = 0
        courses_seen_in_pdf = set()

        for page in file.pages:
            page_text = page.extract_text() or ''
            for line in page_text.split('\n'):
                course_found = name_pattern.match(line.strip())
                if course_found:
                    course_code = course_found.group(1).strip().upper()
                    course_name = course_found.group(2).strip()

                    if course_code in courses_seen_in_pdf:
                        continue
                    courses_seen_in_pdf.add(course_code)
                    
                    if Course.check_course_code_spelling(course_code):
                        course_prefix = course_code.split()[0]
                        course_faculty = cls.FACULTIES.get(course_prefix, 'other')

                        course, course_new = Course.objects.get_or_create(
                            course_code = course_code,
                            defaults={
                                'course_name': course_name,
                                'course_faculty': course_faculty,
                            }
                        )
                        if course_new:
                            num_of_created += 1
                        else:
                            num_of_skipped += 1

        return num_of_created, num_of_skipped

                        
                        


        
    


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