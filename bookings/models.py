from django.db import models
from decimal import Decimal
from django.conf import settings
from django.utils import timezone
from accounts.models import Course

class Booking(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_bookings')

    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tutor_bookings')

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='course_bookings')

    time_slot = models.ForeignKey('Available_Slots', on_delete=models.PROTECT, related_name='bookings') 

    student_note = models.CharField(max_length=255, blank=True, default='')

    session_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED_STUDENT = 'cancelled_by_student', 'Cancelled by Student'
        CANCELLED_TUTOR = 'cancelled_by_tutor', 'Cancelled by Tutor'
        COMPLETED = 'completed', 'Completed'
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.PENDING)

    requested_at = models.DateTimeField(auto_now_add=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    cancellation_reason = models.TextField(blank=True, default='')

    def __str__(self):
        return f"Booking #{self.id} | {self.student.email} -> {self.tutor.email} ({self.status})"

    def confirm(self):

    def cancel_by_student(self, reason=''):

    def cancel_by_tutor(self, reason=''):

    def mark_as_completed(self):

    @staticmethod
    def calculate_price_per_session(hourly_rate, start_time, end_time):
    
    def unblock_booking(self):