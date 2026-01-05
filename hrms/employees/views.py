from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsHR
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsHR]
