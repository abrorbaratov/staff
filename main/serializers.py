from rest_framework import serializers
from .models import Department, Employee, JobTitle


class DepartmentSerializer(serializers.ModelSerializer):

    sub_departments = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ["id", "name", "sub_departments"]

    def get_sub_departments(self, obj):
        sub_departments = obj.sub_departments.all()
        if sub_departments:
            return DepartmentSerializer(sub_departments, many=True).data
        return None


class EmployeeSerializer(serializers.ModelSerializer):

    job_title = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "employment_date",
            "salary",
            "job_title",
        ]
