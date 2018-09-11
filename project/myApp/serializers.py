from rest_framework import serializers

from myApp.models import Student, Grade

# 给学生类创建序列化类
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name", "sex", "age", "contend", "isDelete", "grade")
# 给班级类创建序列化类
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ("id", "name", "boyNum", "girlNum", "isDelete")