from django.shortcuts import redirect, render
from app.models import *
from django.contrib import messages
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
