from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=600)

    def __str__(self):
        return self.email


class category(models.Model):
    cname=models.CharField(max_length=38)
    cpic=models.ImageField(upload_to='static/pcategory/', default="")
    cdate=models.DateField()


class gallery(models.Model):
    pdes=models.CharField(max_length=200)
    gpic=models.ImageField(upload_to='static/gallery/',default="")
    gdate=models.DateField()

class recruiterss(models.Model):
    name=models.CharField(max_length=200)
    rpic=models.ImageField(upload_to='static/recruiters/',default="")
    rdate=models.DateField()

class courses(models.Model):
    cname=models.CharField(max_length=200)
    cpic=models.ImageField(upload_to='static/coure',default="")
    cdate=models.DateField()
    cadmission = models.CharField(max_length=100)
    cduration = models.CharField(max_length=100)
    chead = models.CharField(max_length=100)
    cseat = models.CharField(max_length=100)
    cdescription = models.CharField(max_length=1000)
    ctotal = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    cdate=models.DateField()

    def __str__(self):
        return self.cname


class placements(models.Model):
    name=models.CharField(max_length=100)
    pcourse=models.ForeignKey(courses,on_delete=models.CASCADE)
    branch=models.CharField(max_length=80)
    cmpname=models.CharField(max_length=80)
    cmplogo=models.ImageField(upload_to='static/placement/',default="")
    city=models.CharField(max_length=100)
    pyear=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    stupic=models.ImageField(upload_to='static/studentpic/',default="")
    pdate=models.DateField()

class ourcourse(models.Model):
    coursename=models.CharField(max_length=100)
    coursepic= models.ImageField(upload_to='static/ourcourses/', default="")






