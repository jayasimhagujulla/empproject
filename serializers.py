from testapp.models import Employee,WorkExperience,Qualifications,projects
from rest_framework import serializers 
class EmployeeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=Employee
        fields='__all__' 

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class QualificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifications
        fields = '__all__'

class projectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'