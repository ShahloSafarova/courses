from django.contrib import admin
from courses.models import CourseModel

# Register your models here.
class CourseModelAdmin(admin.ModelAdmin):
    search_fields = ['course_name', 'short_description', 'price']
    list_display = ['course_name']

admin.site.register(CourseModel)