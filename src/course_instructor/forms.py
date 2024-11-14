from django import forms
from course_details.models import Course, CourseContent

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration']  # Fields to be edited by the instructor


class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields = ['title', 'video', 'content_type', 'order', 'additional_resources']
