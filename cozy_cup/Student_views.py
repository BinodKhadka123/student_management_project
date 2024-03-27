from django.shortcuts import redirect, render
from app.models import *
from django.contrib import messages
from django.core.cache import cache
def Home(request):
    return render(request,'Student/home.html')
# Rename the view function to avoid the naming conflict
def Student_notification_send(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notifications = Student_notification.objects.filter(student_id=student_id)
        context = {
            'notifications': notifications
        }
    return render(request, 'Student/notification.html', context)
def Student_notification_mark_as_done(request):
    return None
def Student_apply_leave(request):
    student=Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        student_leave_history = Student_leave.objects.filter(student_id = student_id)
        print(student_leave_history)
        context={
            'student_leave_history':student_leave_history
        }
        print(student_leave_history)
    
    return render(request,'Student/apply_leave.html',context)
def Student_apply_leave_save(request):
     if request.method == "POST":
      leave_date = request.POST.get('leave_date')
      leave_message=request.POST.get('leave_message')
      student_id=Student.objects.get(admin = request.user.id)
      print(student_id)
      print(leave_date)
      print(leave_message)
      student_leave = Student_leave(
          student_id = student_id,
          data = leave_date,
          message = leave_message,
          
      )
      student_leave.save()
      messages.success(request,'Leave Sucessfully sent')
    
      return redirect('leave')
def view_student_bills(request):
    # Retrieve the logged-in student
    student = request.user.student

    # Retrieve billing records for the student
    bills = Billing.objects.filter(student=student)

    # Pass billing information to the template
    context = {
        'student': student,
        'bills': bills
    }
    return render(request, 'Student/view_bills.html', context)
def Student_view_attendence(request):
    student = Student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    
    get_subject = None
    
    # Initialize attendance report outside the conditional block
    attendence_report = None
    
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            
            # Generate a unique cache key for the student and subject combination
            cache_key = f"attendance_{student.id}_{subject_id}"
            
            # Check if the attendance report is cached
            cached_attendance_report = cache.get(cache_key)
            
            if cached_attendance_report:
                # If cached, retrieve from cache
                attendence_report = cached_attendance_report
            else:
                # If not cached, fetch from database
                attendence_report = AttendenceReport.objects.filter(student_id=student, attendence_id__subject_id=subject_id)
                
                # Store fetched report in cache with the generated cache key
                cache.set(cache_key, attendence_report)
    
    context = {
        'subject': subject,
        'action': action,
        'get_subject': get_subject,
        'attendence_report': attendence_report
    }
    
    print(subject)
    
    return render(request, 'Student/view_attendence.html', context)

def Student_view_result(request):
    mark = None
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id=student)
    
    # Initialize variables before the loop
    assignment_mark = 0
    exam_mark = 0
    
    # Loop through the result queryset
    for i in result:
        assignment_mark += i.assignment_mark
        exam_mark += i.exam_mark
    
    # Calculate the total mark
    mark = assignment_mark + exam_mark
    
    context = {
        'result': result,
        'mark': mark
    }
    
    return render(request, 'Student/view_result.html', context)
