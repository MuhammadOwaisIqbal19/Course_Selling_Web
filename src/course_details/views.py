# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied
# from course_details.models import Course, Enrollment
# from django.contrib import messages

# @login_required
# def enroll_in_course(request, course_id):
#     # Fetch the course based on the provided course_id
#     course = get_object_or_404(Course, id=course_id)

#     # Check if the user is already enrolled
#     if Enrollment.objects.filter(student=request.user.profile, course=course).exists():
#         messages.error(request, "You are already enrolled in this course.")
#         return redirect('course_details', course_id=course.id)

#     # Prevent instructors from enrolling in their own course
#     if request.user.profile == course.instructor:
#         raise PermissionDenied("Instructors cannot enroll in their own courses.")

#     # Create an enrollment record
#     enrollment = Enrollment.objects.create(student=request.user.profile, course=course)
#     messages.success(request, f"You have successfully enrolled in {course.title}!")
    
#     return redirect('course_details', course_id=course.id)
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError
# from course_details.models import Course, Enrollment
# from main.models import Profile

# @login_required(login_url='registration/login/')
# def buy_course(request, course_id):
#     # Fetch the course the user is trying to buy
#     course = get_object_or_404(Course, id=course_id)

#     # Get the current user profile (assuming the user is logged in)
#     user_profile = request.user.profile

#     # Check if the user is already enrolled in the course
#     if Enrollment.objects.filter(student=user_profile, course=course).exists():
#         # If already enrolled, redirect to the course details page
#         return redirect('views/course_detail', course_id=course.id)

#     # Enroll the user in the course (simulating a purchase)
#     try:
#         Enrollment.objects.create(student=user_profile, course=course)
#         # Redirect to a success page or course detail page
#         return render(request, 'registration/buy_success.html', {'course': course})
#     except IntegrityError:
#         # This handles any edge cases if the student is somehow double enrolled
#         return redirect('views/course_detail', course_id=course.id)
