from django.shortcuts import get_object_or_404, redirect, render
from app.models import *
from django.contrib import messages
def Home(request):
    return render(request,'Staff/home.html')
def Notification(request):
    # Filter staff based on the logged-in user's ID
    staff = Staff.objects.filter(admin=request.user.id)
    
    notifications = []
    
    # Iterate over staff members
    for staff_member in staff:
        staff_id = staff_member.id
        
        # Filter notifications for the current staff member
        staff_notifications = Staff_notification.objects.filter(staff_id=staff_id)
        
        # Iterate over notifications for the current staff member
        for notification in staff_notifications:
            # Append each notification's message to the list
            notifications.append(notification.message)
            
            # Print the message
            print(notification.message)
        
    context = {
        'notifications': notifications
    }
    
    return render(request, 'Staff/notification.html', context)
def Staff_notification_mark_as_done(request,status):
    notification = Staff_notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')
def Staff_apply_leave(request):
    staff=Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)
        print(staff_leave_history)
        context={
            'staff_leave_history':staff_leave_history
        }
        print(staff_leave_history)
        return render(request,'Staff/apply_leave.html',context)
def Staff_apply_leave_save(request):
    if request.method == "POST":
      leave_date = request.POST.get('leave_date')
      leave_message=request.POST.get('leave_message')
      staff=Staff.objects.get(admin = request.user.id)
      leave = Staff_leave(
          staff_id = staff,
          data = leave_date,
          message = leave_message,
          
      )
      leave.save()
      messages.success(request,'Leave Sucessfully sent')
    return redirect('apply_leave')
def Staff_add_result(request):
    staff = Staff.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff_id = staff)
    session_year = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
           subject_id = request.POST.get('subject_id')
           session_year_id = request.POST.get('session_year_id')

           get_subject = Subject.objects.get(id = subject_id)
           get_session = Session.objects.get(id = session_year_id)
           print(get_subject)
           for i in subjects:
               student_id = i.course.id
               students = Student.objects.filter(course_id = student_id)


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }
    print(students)

    return render(request,'Staff/add_result.html',context)


def Staff_save_result(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.subject_assignment_marks = assignment_mark
            result.subject_exam_marks = Exam_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = StudentResult(student_id=get_student, subject_id=get_subject, exam_mark=Exam_mark, assignment_mark=assignment_mark)

            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')

def Staff_take_attendence(request):
    staff = Staff.objects.get(admin=request.user)
    subjects = Subject.objects.filter(staff=staff)
    session_years = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
           subject_id = request.POST.get('subject_id')
           session_year_id = request.POST.get('session_year_id')

           get_subject = Subject.objects.get(id = subject_id)
           get_session = Session.objects.get(id = session_year_id)

           subjects = Subject.objects.filter(id = subject_id)
           for i in subjects:
               student_id = i.course.id
               students = Student.objects.filter(course_id = student_id)

    

    context = {
       'staff': staff,
        'subjects': subjects,
        'session_years': session_years,
        'get_session': get_session,  # Corrected: Removed extra space before variable name
        'get_subject': get_subject,  # Corrected: Removed extra space before variable name
        'action': action,
        'students':students,
        
    }

    return render(request, 'Staff/take_attendence.html', context)
def Staff_save_attendence(request):
      if request.method == "POST":
       subject_id = request.POST.get('subject_id')
       session_year_id = request.POST.get('session_year_id')
       attendence_date = request.POST.get('attendence_date')
       student_id = request.POST.getlist('student_ids')
       print(student_id)
       get_subject = Subject.objects.get(id = subject_id)
       get_session = Session.objects.get(id = session_year_id)
       
       attendence=Attendance(
           subject_id=get_subject,
           attendence_data=attendence_date,
           session_year_id=get_session,
       )
       attendence.save()
       print(student_id)
       for i in student_id:
           stud_id = i
           int_stud =int(stud_id)
           p_students=Student.objects.get(id = int_stud)
           attendence_report=AttendenceReport(
               student_id=p_students,
               attendence_id=attendence,
           )
           attendence_report.save()
      return redirect('take_attendence')
def Staff_view_attendence(request): 
    staff = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff=staff)
    session_years = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    attendence_date = None
    attendence_report=None
    
    if action is not None:
        if request.method == "POST":
           subject_id = request.POST.get('subject_id')
           session_year_id = request.POST.get('session_year_id')
           attendence_date = request.POST.get('attendence_date')

           get_subject = Subject.objects.get(id = subject_id)
           get_session = Session.objects.get(id = session_year_id)

           attendence=Attendance.objects.filter(subject_id=get_subject,attendence_data=attendence_date)
           for i in attendence:
               attendence_id=i.id
               attendence_report=AttendenceReport.objects.filter(attendence_id=attendence_id)
               
    
    context={
        'subjects':subjects,
        'session_years':session_years,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'attendence_date':attendence_date,
        'attendence_report':attendence_report
    }
    print(attendence_report)
    return render(request,'Staff/view_attendence.html',context)