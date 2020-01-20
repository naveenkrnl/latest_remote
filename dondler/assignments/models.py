from django.db import models
from books.models import Subject
from django.contrib.auth import get_user_model

User= get_user_model()
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

class Assignment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.TextField(max_length=1000,null=True,blank=True)
    link=models.URLField(null=True,blank=True)
    last_date=models.DateTimeField()
    semester=models.CharField(max_length=200,choices=SEMESTER_CHOICES,default="7")
    files=models.FileField(upload_to='assignments/',null=True,blank=True)
    def __str__(self):
        return self.name

class SubmitAssignment(models.Model):
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=1000,null=True,blank=True)
    link=models.URLField(null=True,blank=True)
    submission_date=models.DateTimeField(auto_now_add=True)
    files=models.FileField(upload_to='submitted-assignments/',null=True,blank=True)
    def __str__(self):
        return self.user.username + " - " +self.assignment.name