from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings  # To reference User and Profile models
from datetime import timedelta
from main.models import Profile  # Assuming Profile is in an app named 'users'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField(default=timedelta(days=30))  # Duration of the course
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='courses_taught')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class CourseContent(models.Model):
    course = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='course_videos/')  # Path to store video files
    content_type = models.CharField(max_length=100, choices=[('video', 'Video'), ('pdf', 'PDF'), ('text', 'Text')])
    order = models.IntegerField()  # To display content in sequence/order
    additional_resources = models.FileField(upload_to='resources/', null=True, blank=True)  # Optional resources
    is_first_video = models.BooleanField(default=False)  # Indicates if this is the first video in the course

    def __str__(self):
        return f"{self.title} ({self.content_type})"    
    
    def save(self, *args, **kwargs):
        # Ensure only one 'is_first_video' is set to True for a course
        if self.is_first_video:
            # Reset other contents for this course to not be the first video
            CourseContent.objects.filter(course=self.course, is_first_video=True).update(is_first_video=False)
        super(CourseContent, self).save(*args, **kwargs)


class Enrollment(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='courses_enrolled')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"

    class Meta:
        unique_together = ('student', 'course')  # Ensure a student can enroll only once per course
