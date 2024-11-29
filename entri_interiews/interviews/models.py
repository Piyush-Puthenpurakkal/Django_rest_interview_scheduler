# interviews/models.py
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Interviewer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AvailableTimeSlot(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.date} ({self.start_time} - {self.end_time})"
