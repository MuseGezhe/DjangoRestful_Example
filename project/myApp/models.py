from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=20)
    boyNum = models.IntegerField()
    girlNum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'grades'


class StudentManage(models.Manager):
    def get_quertset(self):
        return super(StudentManage, self).get_quertset(
            ).filter(isDelete=False)
class Student(models.Model):
    objects = StudentManage()
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField()
    contend = models.CharField(max_length=40)
    grade = models.ForeignKey('grade')
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'students'



