from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.


class CompanyName(models.Model):
    company_name = models.TextField(max_length=50)


class UserComapny(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company_id = models.ForeignKey(CompanyName,on_delete=models.CASCADE)

class User_Group(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    Group_id=models.ForeignKey(Group, on_delete=models.CASCADE)


class Expert(models.Model):
    name=models.TextField(max_length=20)
    Designation=models.TextField(max_length=50)
    CompanyName=models.ForeignKey(CompanyName, on_delete=models.CASCADE)
    Field_of_Experience=models.IntegerField()
    Skill=models.TextField(max_length=50)
    Personal_Email=models.TextField(max_length=20)
    mobile=models.IntegerField()
    Profile_piture=models.TextField
    about=models.TextField(max_length=100)
    password=models.TextField(max_length=20)
    Icard_Picture=models.TextField(null=True)


class Student(models.Model):
    Student_id = models.IntegerField()
    name = models.TextField(max_length=20)
    Collage=models.TextField(max_length=50)
    Year_Experience=models.IntegerField()
    Qualification=models.TextField(max_length=50)
    Personal_Email=models.TextField(max_length=20)
    mobile=models.IntegerField()
    Profile_piture=models.TextField()
    password=models.TextField(max_length=20)


class Expert_Student_Block(models.Model):
    Expert_id=models.ForeignKey(Expert, on_delete=models.CASCADE)
    Student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    is_block=models.TextField()


class Student_block_count(models.Model):
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    block_count=models.IntegerField()


class Expert_Following(models.Model):
    Student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    Expert_id=models.ForeignKey(Expert, on_delete=models.CASCADE)
    Is_follow=models.TextField(max_length=20)
    Is_follow_accepted=models.TextField(max_length=20)


class AddLecture(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    expert_id = models.ForeignKey(Expert, on_delete=models.CASCADE)


class StudentLectureAttended(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    expert_id = models.ForeignKey(Expert, on_delete=models.CASCADE)
    lecture_id = models.ForeignKey(AddLecture, on_delete=models.CASCADE)


class LectureHistory(models.Model):
    lecture_id = models.ForeignKey(AddLecture, on_delete=models.CASCADE)
    student_count = models.IntegerField()
    student_list = models.TextField()
