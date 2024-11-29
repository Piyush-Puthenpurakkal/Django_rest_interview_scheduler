from django.contrib import admin
from .models import *

# Customize Candidate admin
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display ID and name
    ordering = ('id',)  # Order by ID

# Customize Interviewer admin
@admin.register(Interviewer)
class InterviewerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display ID and name
    ordering = ('id',)

# Customize AvailableTimeSlot admin
@admin.register(AvailableTimeSlot)
class AvailableTimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'interviewer', 'date', 'start_time', 'end_time')
    ordering = ('id',)
