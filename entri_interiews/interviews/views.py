from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate, Interviewer, AvailableTimeSlot
from .serializers import AvailableTimeSlotSerializer


class RegisterTimeSlotView(APIView):
    """
    API to register available time slots for candidates/interviewers.
    """
    def post(self, request):
        serializer = AvailableTimeSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Time slot registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSchedulableTimeSlotsView(APIView):
    """
    API to get schedulable interview time slots.
    """
    def get(self, request):
        candidate_id = request.query_params.get('candidate_id')
        interviewer_id = request.query_params.get('interviewer_id')

        if not candidate_id or not interviewer_id:
            return Response({"error": "Candidate ID and Interviewer ID are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch time slots for candidate and interviewer
        candidate_slots = AvailableTimeSlot.objects.filter(candidate_id=candidate_id)
        interviewer_slots = AvailableTimeSlot.objects.filter(interviewer_id=interviewer_id)

        common_slots = []

        for c_slot in candidate_slots:
            for i_slot in interviewer_slots:
                if c_slot.date == i_slot.date:
                    # Find the overlapping time range
                    start_time = max(c_slot.start_time, i_slot.start_time)
                    end_time = min(c_slot.end_time, i_slot.end_time)

                    # Generate hourly slots if there is overlap
                    current_time = datetime.combine(c_slot.date, start_time)
                    end_time = datetime.combine(c_slot.date, end_time)

                    while current_time + timedelta(hours=1) <= end_time:
                        slot = (
                            current_time.time(),
                            (current_time + timedelta(hours=1)).time(),
                        )
                        common_slots.append(slot)
                        current_time += timedelta(hours=1)

        return Response({"schedulable_slots": common_slots}, status=status.HTTP_200_OK)