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
    try:
        staff = Staff.objects.get(admin=request.user)
        subjects = Subject.objects.filter(staff=staff)
        session_year = Session.objects.all()
    except Staff.DoesNotExist:
        staff = None
        subjects = None
        session_year = None

    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session.objects.get(id=session_year_id)

            # Retrieve students for the selected subject and session year
            students = Student.objects.filter(course_id=get_subject.course, session_year_id=get_session)

    print("Number of students:", len(students))  # Debugging statement

    context = {
        'staff': staff,
        'subjects': subjects,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students,
    }
    print(students)

    return render(request, 'Staff/add_result.html', context)


# def Staff_save_result(request):
#     if request.method == "POST":
#         subject_id = request.POST.get('subject_id')
#         session_year_id = request.POST.get('session_year_id')
#         student_id = request.POST.get('student_id')
#         assignment_mark = request.POST.get('assignment_mark')
#         Exam_mark = request.POST.get('Exam_mark')

#         get_student = Student.objects.get(admin = student_id)
#         get_subject = Subject.objects.get(id=subject_id)

#         check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
#         if check_exist:
#             result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
#             result.subject_assignment_marks = assignment_mark
#             result.subject_exam_marks = Exam_mark
#             result.save()
#             messages.success(request, "Successfully Updated Result")
#             return redirect('staff_add_result')
#         else:
#             result = StudentResult(student_id=get_student, subject_id=get_subject, subject_exam_marks=Exam_mark,
#                                    subject_assignment_marks=assignment_mark)
#             result.save()
#             messages.success(request, "Successfully Added Result")
#             return redirect('staff_add_result')

def Staff_take_attendence(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    print("Staff ID:", staff_id)  # Print staff ID to check if it's successfully retrieved
    
    # Filter subjects based on the staff_id
    subjects = Subject.objects.filter(staff=staff_id)
    
    # Print subjects to check if they are retrieved successfully
    print("Subjects:", subjects)
    session_year=Session.objects.all()
    context={
       ' subject':subjects,
       ' session_year':session_year,
    }
    print(subjects)
    print(session_year)
    return render(request,'Staff/take_attendence.html',context)