from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class CustomUser(AbstractUser):
    UniqueId = models.CharField(primary_key=True, max_length=15, null=False,)

    def __str__(self):
        return self.username


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class LectureRecord(models.Model):
    lr_id = models.AutoField(primary_key=True)
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    course_number = models.CharField(max_length=50, null=False)
    course_name = models.CharField(max_length=50, null=False, default='TBD')
    # instructer_id = models.CharField(max_length=50, null=False)
    instructer_id = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    instructer_name = models.CharField(max_length=100, null=False)
    time = models.CharField(max_length=100, null=False)
    day = models.CharField(max_length=100, null=False)

class FormData(models.Model):
    fd_id = models.ForeignKey("LectureRecord", on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    course_number = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    assignment_given = models.CharField(max_length=100)
    assignment_collected = models.CharField(max_length=100)
    assignment_distributed = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    instructer_id = models.CharField(max_length=100)
    instructer_name = models.CharField(max_length=100)
    date = models.DateField(default=date.today)

