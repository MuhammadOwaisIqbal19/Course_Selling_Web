

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Course,Enrollment,CourseContent


class CourseAdmin(admin.ModelAdmin):
    pass

class CourseContentAdmin(admin.ModelAdmin):
    pass

class EnrollmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(CourseContent, CourseContentAdmin)
