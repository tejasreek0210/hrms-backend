from datetime import date
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "HR":
            return Attendance.objects.all()
        return Attendance.objects.filter(employee__user=user)

    def create(self, request, *args, **kwargs):
        employee = request.user.employee
        today = date.today()

        if Attendance.objects.filter(employee=employee, date=today).exists():
            return Response(
                {"detail": "Attendance already marked for today"},
                status=status.HTTP_400_BAD_REQUEST
            )

        attendance = Attendance.objects.create(employee=employee, date=today)
        serializer = self.get_serializer(attendance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
