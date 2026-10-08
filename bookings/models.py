from django.db import models

# Create your models here.

# ==========================================
# VON MIR (DJANGO DEFAULTS)
# ==========================================

# ==========================================
# VON EUCH (AUS DEM PDF)
# ==========================================

# Available Slots
#     ID
#     tutor ID
#     start Time
#     end Time
#     salary
#     locationType (ONLINE, IN-PERSON)
#     status (Available, Booked, pending, Cancelled)
#     create Slot()
#     update Slot()
#     cancel Slot()
#     is Available()
#     check for time overlap()
#     check Start & Endtime()
#     calculate price suggestion()

# Booking
#     ID
#     Slot ID
#     Student ID
#     tutor ID
#     price
#     course / topic
#     status (Pending, Canceled By..., Completed)
#     requested at
#     canceled at
#     completed at
#     (cancellation Reason)
#     create Booking Request()
#     cancel by Student()
#     cancel by Tutor()
#     mark as Completed()
#     ask for Review()
#     calculate Price per Session()
#     unblock Booking()
