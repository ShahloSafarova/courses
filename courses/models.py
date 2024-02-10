from django.db import models


# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=25)
    short_description = models.TextField()
    course_price = models.DecimalField(max_digits=8,decimal_places=2)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name

