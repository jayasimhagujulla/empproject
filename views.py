from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404

class CreateEmployeeAPIView(APIView):
    """
    API endpoint to create a new employee.
    """
    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Employee created successfully",
                    "success": True
                }, status=status.HTTP_201_CREATED)
            return Response({
                "message": "Invalid data",
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "Employee creation failed",
                "success": False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateEmployeeAPIView(APIView):
    """
    API endpoint to update an employee.
    """
    def put(self, request, employee_id):
        try:
            employee = get_object_or_404(Employee, id=employee_id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Employee details updated successfully",
                    "success": True
                }, status=status.HTTP_200_OK)
            return Response({
                "message": "Invalid data",
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({
                "message": "No employee found with this ID",
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "message": "Employee updation failed",
                "success": False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListEmployeesAPIView(APIView):
    """
    API endpoint to get a list of all employees.
    """
    def get(self, request):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response({
                "message": "Employee details found",
                "success": True,
                "employees": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Error retrieving employees",
                "success": False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteEmployeeAPIView(APIView):
    """
    API endpoint to delete an employee.
    """
    def delete(self, request, employee_id):
        try:
            employee = get_object_or_404(Employee, id=employee_id)
            employee.delete()
            return Response({
                "message": "Employee deleted successfully",
                "success": True
            }, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({
                "message": "No employee found with this ID",
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "message": "Employee deletion failed",
                "success": False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
