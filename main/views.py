from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .paginations import EmployeePagination


class ListEmployees(ListAPIView):
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get_queryset(self):
        dep = self.request.query_params.get("dep")
        if dep is not None:
            return Employee.objects.select_related("job_title").filter(
                job_title__department_id=dep
            )
        return Employee.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListDepartments(APIView):

    def get(self, request, format=None):
        departments = Department.objects.filter(
            parent_department=None
        ).prefetch_related(
            Prefetch(
                "sub_departments",
                queryset=Department.objects.prefetch_related(
                    Prefetch(
                        "sub_departments",
                        queryset=Department.objects.prefetch_related(
                            Prefetch(
                                "sub_departments",
                                queryset=Department.objects.prefetch_related(
                                    Prefetch(
                                        "sub_departments",
                                        queryset=Department.objects.prefetch_related(
                                            "sub_departments"
                                        ),
                                    )
                                ),
                            )
                        ),
                    )
                ),
            )
        )
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
