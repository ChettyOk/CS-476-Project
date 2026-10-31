# .\venv\Scripts\Activate.ps1
from django.db import models
import re
import json
import os
import pypdf
from .constants import FACULTIES

#import for users
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models.functions import Lower

class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True, db_index=True)
    course_name = models.CharField(max_length=200, db_index=True)
    course_faculty = models.CharField(max_length=50, db_index=True)

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
    def create_course(cls, course_code, course_name):

        if not cls.check_course_code_spelling(course_code):
            raise ValueError(f'invalid course code')
        
        match = re.match(r"^([A-Z]{2,4})\s*(\d{3})$", course_code.strip().upper())
        course_code = f"{match.group(1)} {match.group(2)}"

        course_prefix = course_code.split()[0]
        course_faculty = cls.FACULTIES.get(course_prefix, 'other')
        
        return cls.objects.create(course_code = course_code, course_name = course_name, course_faculty = course_faculty)

    @classmethod
    def get_courses_from_file(cls, pdf_file):
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
# create user accounts identified by email
class UserManager(BaseUserManager):

    @classmethod
    def normalize_email(cls, email):
        return super().normalize_email(email).strip().lower()

    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)

        if not email:
            raise ValueError("An email address is required.")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email):
        email = self.normalize_email(email)
        return self.get(email__iexact=email)

# shared account model for students and tutors
class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        TUTOR = "tutor", "Tutor"

    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        blank=True,
        default="",
    )
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("email"),
                name="accounts_user_email_ci_unique",
            ),
        ]

    def __str__(self):
        return self.email

    #check whether the user's email has a valid format
    def check_email(self):

        try:
            validate_email(self.email)
        except ValidationError:
            return False

        return True

    # return the user's role
    def has_role(self, role):

        return role in self.Role.values and self.role == role

    #switch the user role
    def switch_role(self, role):
        """Change the active role without saving the user."""

        if role not in self.Role.values:
            raise ValueError("Role must be 'student' or 'tutor'.")

        self.role = role


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
