from django.urls import path
from .views import RegisterTimeSlotView, GetSchedulableTimeSlotsView

urlpatterns = [
    path('register-time-slot/', RegisterTimeSlotView.as_view(), name='register_time_slot'),
    path('get-schedulable-slots/', GetSchedulableTimeSlotsView.as_view(), name='get_schedulable_slots'),
]