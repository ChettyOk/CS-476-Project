from django.db import models

# Create your models here.
# Variables / classes / intern functions

# ==========================================
# VON MIR (DJANGO DEFAULTS & ERLÄUTERUNGEN)
# ==========================================
# Hier unten beginnt exakt der Text aus eurem PDF. 
# Ich habe meine hinzugefügten Wörter wie "Variables:" 
# oder "Functions:" sowie die "class"-Schlüsselwörter entfernt.

# ==========================================
# VON EUCH (AUS DEM PDF)
# ==========================================

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