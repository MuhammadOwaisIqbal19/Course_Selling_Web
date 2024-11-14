from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from course_details.models import Course, CourseContent,Enrollment
from .forms import CourseForm, CourseContentForm
from course_instructor.models import Purchase

# Create a new course (Instructor only)
@login_required(login_url='registration/login/')
def create_course(request):
    if not request.user.profile.is_instructor:
        raise PermissionDenied("You must be an instructor to create a course.")
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user.profile  # Link the course to the instructor
            course.save()
            return redirect('course_details')  # Redirect to the course details page or list
    else:
        form = CourseForm()

    return render(request, 'registration/create_course.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import CourseContentForm  # Assuming you have a form for CourseContent

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseContentForm
from course_details.models import Course  # Assuming Course is the model for courses

@login_required(login_url='registration/login/')
def add_update_content(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Retrieve the course using the course_id
    if request.method == "POST":
        form = CourseContentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the content but associate it with the retrieved course
            course_content = form.save(commit=False)
            course_content.course = course  # Associate the course with the content
            course_content.save()
            return redirect('success_page')  # Redirect after saving
        else:
            print(form.errors)
    else:
        form = CourseContentForm()

    return render(request, 'registration/add_content.html', {'form': form, 'course': course})

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import PermissionDenied

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # If the user is already logged in, redirect them

    def form_valid(self, form):
        # Authenticate the user and check if they are an instructor
        user = form.get_user()

        if user.profile.is_instructor:  # Check if the user is an instructor
            login(self.request, user)  # Log the user in
            return redirect('create_course')  # Redirect to create_course view
        else:
            raise PermissionDenied("You must be an instructor to access this page.")


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Course,Purchase
from course_details.models import Enrollment



# @login_required(login_url='registration/login/')
# def buy_course(request, course_id):
#     # Fetch the course based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)

#     # Check if the user has already bought the course
#     if Purchase.objects.filter(student=request.user.profile, course=course).exists():
#         messages.error(request, "You have already purchased this course.")
#         return redirect('registration/course_details', course_id=course.id)

#     # Create a purchase record
#     purchase = Purchase.objects.create(student=request.user.profile, course=course)
    
#     # Automatically enroll the user in the course after purchase
#     if not Enrollment.objects.filter(student=request.user.profile, course=course).exists():
#         Enrollment.objects.create(student=request.user.profile, course=course)

#     # Success message and redirect to course details page
#     messages.success(request, f"You have successfully purchased and enrolled in {course.title}!")
#     return redirect('registration/course_details', course_id=course.id)





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import VideoProgress, CourseContent, Profile

@csrf_exempt
def mark_video_watched(request):
    if request.method == 'POST':
        try:
            # Parse the request data (assuming it's in JSON format)
            data = json.loads(request.body)
            video_id = data.get('video_id')
            student_id = data.get('student_id')
            

            # Fetch the video and student from the database
            video = get_object_or_404(CourseContent, id=video_id)
            student = get_object_or_404(Profile, id=student_id)

            # Get or create the video progress for the student and video
            video_progress, created = VideoProgress.objects.get_or_create(
                student=student, 
                video=video,
                defaults={'watched': False}  # Default is watched=False for all videos initially
            )
            

            # Update the progress to watched=True only when the user watches the video
            video_progress.watched = True
            video_progress.save()
            

            # Return success response
            return JsonResponse({'message': 'Video marked as watched successfully!'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
