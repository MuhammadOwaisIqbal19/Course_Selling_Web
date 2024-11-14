

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from main.models import Profile
from course_details.models import Course,CourseContent
from django.core.exceptions import ValidationError


class Purchase(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='purchased_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='purchases')
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} bought {self.course.title}"
    
    class Meta:
        unique_together = ('student', 'course')  # Ensure a user can buy a course only once


class VideoProgress(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

class Quiz(models.Model):
    course_content = models.OneToOneField(CourseContent, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def clean(self):
        """
        Custom validation to ensure a quiz has no more than 10 questions.
        """
        if self.questions.count() > 10:
            raise ValidationError('A quiz can have a maximum of 10 questions.')

    def save(self, *args, **kwargs):
        # Ensure that the clean method is called before saving
        self.clean()
        super().save(*args, **kwargs)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=255, choices=[
        ('a', 'Option A'),
        ('b', 'Option B'),
        ('c', 'Option C'),
        ('d', 'Option D'),
    ])

    def __str__(self):
        return f"Question {self.id}: {self.question_text}"

    # Optionally, you can add a method to check if an answer is correct
    def check_answer(self, answer):
        return answer.lower() == self.correct_answer        

class QuizAttempt(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    passed = models.BooleanField(default=False)

class QuizAccess(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    can_take_quiz = models.BooleanField(default=False)

class NextVideoAccess(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    current_video = models.ForeignKey(CourseContent, related_name='current_video', on_delete=models.CASCADE)
    next_video = models.ForeignKey(CourseContent, related_name='next_video', on_delete=models.CASCADE)
    can_access = models.BooleanField(default=False)
