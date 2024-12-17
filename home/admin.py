from django.contrib import admin

# Register your models here.
from course.models import Course
from course.models import Subject

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

admin.site.register(Course,CourseAdmin)
admin.site.register(Subject)
