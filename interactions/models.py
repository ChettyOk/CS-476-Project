from django.db import models

# Create your models here.

# ==========================================
# VON MIR (DJANGO DEFAULTS)
# ==========================================

# ==========================================
# VON EUCH (AUS DEM PDF)
# ==========================================

# Notifications
#     ID
#     recipient ID
#     type (Cancellation, Confirmation, ...)
#     title
#     message
#     related Booking ID
#     created At
#     sender ID
#     status in Web
#     create Notification()
#     get contact information()
#     get unread Notifications()
#     trigger Notification()
#     trigger Email()
#     mark As read()
#     rating notification()

# Ratings
#     ID
#     reviewer ID
#     reviewer Role
#     reviewed Person ID
#     rating
#     created At
#     (comment)
#     status (reviewed, not reviewed)
#     create Review()
#     check for Booking()
#     update Tutor Rating()
#     update Student Rating()
