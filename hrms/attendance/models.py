from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()
    check_in_time = models.TimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.employee_id} - {self.date}"
 