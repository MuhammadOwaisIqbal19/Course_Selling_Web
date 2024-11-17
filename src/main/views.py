from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from .models import Listing,LikedListing
# from .forms import ListingForm
# from users.forms import LocationForm
# from django.contrib import messages
# from .filters import ListingFilter
from importlib import reload
from django.http import JsonResponse
# from course_details.models import Course


def if_is_instructor(request):
    return render(request,"views/if_is_instructor.html")

from django.shortcuts import render
from course_details.models import Course  # Import the Course model

def main_page(request):
    # Fetch all courses
    courses = Course.objects.all()  # You can filter this as per your requirements

    # Pass the courses to the template
    return render(request, 'views/main_page.html', {'courses': courses})

# views.py
from django.shortcuts import render, get_object_or_404
# from course_details.models import Course
from course_instructor.models import Purchase
from course_details.models import Enrollment
# def course_detail(request, course_id):
#     # Get the course object based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)

#     # Get the course content (videos, PDFs, etc.) associated with this course
#     course_contents = course.contents.all()

#     # Pass the course and its contents to the template for rendering
#     return render(request, 'views/course_detail.html', {
#         'course': course,
#         'course_contents': course_contents
#     })

from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404
from course_instructor.models import  Quiz, QuizAttempt
from course_details.models import Course,CourseContent

from django.shortcuts import render, get_object_or_404
from course_instructor.models import Quiz, QuizAttempt
from course_details.models import Course, CourseContent

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course_contents = CourseContent.objects.filter(course=course)
    first_video = course_contents.filter(is_first_video=True).first()
    
    quiz = None  # Initialize quiz variable

    if request.user.is_authenticated:
        # Check if the user has already completed the first video quiz
        if first_video:
            quiz = Quiz.objects.filter(course_content=first_video).first()  # Update this line
            quiz_attempt = QuizAttempt.objects.filter(student=request.user.profile, quiz=quiz).first()
        
            if quiz_attempt and quiz_attempt.passed:
                # Allow the user to watch other videos if quiz passed
                can_access_all_videos = True
            else:
                # Allow access only to the first video
                can_access_all_videos = False
        else:
            can_access_all_videos = False
    else:
        # Non-authenticated users can only access the first video
        can_access_all_videos = False

    context = {
        'course': course,
        'course_contents': course_contents,
        'first_video': first_video,
        'can_access_all_videos': can_access_all_videos,
        'quiz': quiz,  # Pass quiz to the template
    }
    return render(request, 'views/course_detail.html', context)



# # @login_required
# def course_detail(request, course_id):
#     # Fetch the course based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)

#     # Check if the user has purchased the course
#     purchase = Purchase.objects.filter(student=request.user.profile, course=course).exists()
    
#     if not purchase:
#         messages.error(request, "You need to purchase this course before you can access it.")
#         return redirect('views/main_page')  # Redirect to a general page, or a specific page where courses are listed
    
#     # Check if the user is enrolled in the course
#     enrollment = Enrollment.objects.filter(student=request.user.profile, course=course).exists()
    
#     if not enrollment:
#         # If the user is not enrolled, automatically enroll them
#         Enrollment.objects.create(student=request.user.profile, course=course)
    
#     # Proceed with rendering course details for the enrolled user
#     context = {
#         'course': course,
#         'course_contents': course.contents.all(),
#         # Add any additional context like course videos, quizzes, etc.
#     }
    
#     return render(request, 'views/course_detail.html', context)
# @login_required(login_url='registration/login/')
# def course_detail(request, course_id):
#     # Fetch the course based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)

#     # Check if the user has purchased the course
#     purchase = Purchase.objects.filter(student=request.user.profile, course=course).exists()
    
#     if not purchase:
#         messages.error(request, "You need to purchase this course before you can access it.")
#         return redirect('main')  # Redirect to a general page, or a specific page where courses are listed
    
#     # Check if the user is enrolled in the course
#     enrollment = Enrollment.objects.filter(student=request.user.profile, course=course).exists()
    
#     if not enrollment:
#         # If the user is not enrolled, automatically enroll them
#         Enrollment.objects.create(student=request.user.profile, course=course)
    
#     # Proceed with rendering course details for the enrolled user
#     context = {
#         'course': course,
#         'course_contents': course.contents.all(),
#         # Add any additional context like course videos, quizzes, etc.
#     }
    
#     return render(request, 'views/course_detail.html', context)




# def course_detail(request, course_id):
#     # Fetch the course based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)
    
#     # Context for both authenticated and unauthenticated users
#     context = {
#         'course': course,
#         'course_contents': None,  # Default to None, contents will be added conditionally
#         'purchase_required': False,  # Default flag for purchase requirement
#     }

#     # If the user is authenticated, check for purchase and enrollment
#     if request.user.is_authenticated:
#         purchase = Purchase.objects.filter(student=request.user.profile, course=course).exists()

#         if not purchase:
#             messages.error(request, "You need to purchase this course before you can access it.")
#             return redirect('main')

#         # Check if the user is enrolled
#         enrollment = Enrollment.objects.filter(student=request.user.profile, course=course).exists()
#         if not enrollment:
#             Enrollment.objects.create(student=request.user.profile, course=course)

#         # Include full course content for authenticated users
#         context['course_contents'] = course.contents.all()
#     else:
#         # Optionally, for unauthenticated users, show a limited preview
#         context['preview_message'] = "Please log in or register to access full course content."

#     return render(request, 'views/course_detail.html', context)



# @login_required(login_url='registration/login/')
# def buy_course(request, course_id):
#     # Fetch the course based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)

#     # Check if the user has already bought the course
#     if Purchase.objects.filter(student=request.user.profile, course=course).exists():
#         messages.error(request, "You have already purchased this course.")
#         return redirect('course_detail', course_id=course.id)

#     # Create a purchase record
#     purchase = Purchase.objects.create(student=request.user.profile, course=course)
    
#     # Automatically enroll the user in the course after purchase
#     if not Enrollment.objects.filter(student=request.user.profile, course=course).exists():
#         Enrollment.objects.create(student=request.user.profile, course=course)

#     # Success message and redirect to course details page
#     messages.success(request, f"You have successfully purchased and enrolled in {course.title}!")
#     return redirect('course_detail', course_id=course.id)

