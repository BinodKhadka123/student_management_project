from django.shortcuts import render
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from . import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.Base, name='base'),
    path('login/',views.Login, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
   path('logout/', views.Logout, name='logout'),
   #profile update
   path('profile/',views.profile,name='profile'),
   path('profile/update/',views.profile_update,name='profile_update'),
    #this is hod pannel
    path('hod/home/', Hod_views.Home, name='Hod_home'),
    
     path('hod/add/student', Hod_views.Add_student, name='Add_student'),
     path('hod/view_student/',Hod_views.View_student, name='View_student'),
     path('hod/edit_student/<str:id>',Hod_views.Edit_student, name='Edit_student'),
      path('hod/update_student/',Hod_views.Update_student, name='Update_student'),
      path('hod/delete_student/<str:admin>/',Hod_views.Delete_student, name='Delete_student'),
    path('hod/add_session/', Hod_views.Add_session, name='Add_session'),
    path('hod/add_course/', Hod_views.Add_course, name='Add_course'),
    path('hod/view_course/', Hod_views.View_course, name='View_course'),
    path('hod/edit_course/<str:id>', Hod_views.Edit_course, name='Edit_course'),
     path('hod/update_course/', Hod_views.Update_course, name='update_course'),
     path('hod/add_staff/',Hod_views.Add_staff, name='Add_staff'),
     path('hod/view_staff/',Hod_views.View_staff, name='View_staff'),
     path('hod/edit_staff/<str:id>', Hod_views.Edit_staff, name='Edit_staff'),
     path('hod/update_staff/',Hod_views.Update_staff, name='Update_staff'),
     path('hod/delete_staff/<str:admin>/',Hod_views.Delete_staff, name='Delete_staff'),
      path('hod/add/subject', Hod_views.Add_subject, name='Add_subject'),
      path('hod/view/subject',Hod_views.View_subject,name='View_subject'),
       path('hod/edit_subject/<str:id>', Hod_views.Edit_subject, name='Edit_subject'),
       path('hod/update_subject/',Hod_views.Update_subject, name='Update_subject'),
       path('hod/delete/subject/<str:id>',Hod_views.Delete_subject,name='Delete_subject'),
       path('hod/add/session',Hod_views.Add_session,name='Add_session'),
        path('hod/view/session',Hod_views.View_session,name='View_session'),
        path('hod/edit_session/<str:id>', Hod_views.Edit_session, name='Edit_session'),
         path('hod/staff/send_notification', Hod_views.Staff_send_notification, name='Staff_send_notification'),
          path('hod/staff/save_notification', Hod_views.Save_staff_notification, name='Save_staff_notification'),
        
         path('hod/staff/leave_view/',Hod_views.Staff_leave_view,name='staff_leave_view'),
          path('hod/staff/approve/leave/<str:id>',Hod_views.Staff_approve_leave,name='staff_approve_leave'),
          path('hod/staff/disapprove/leave/<str:id>',Hod_views.Staff_disapprove_leave,name='staff_disapprove_leave'),
          
          path('hod/student/leave_view/',Hod_views.Student_leave_view,name='student_leave_view'),
          path('hod/student/approve/leave/<str:id>',Hod_views.Student_approve_leave,name='student_approve_leave'),
          path('hod/student/disapprove/leave/<str:id>',Hod_views.Student_disapprove_leave,name='student_disapprove_leave'),
          
          
           path('hod/student/send_notification', Hod_views.Student_send_notification, name='Student_send_notification'),
            path('hod/student/save_notification', Hod_views.Save_student_notification, name='Save_student_notification'),
        
        #this ia staff url
        path('staff/home/', Staff_views.Home, name='staff_home'),  
        path('staff/notification',Staff_views.Notification,name='notification'),
        path('staff/apply/leave',Staff_views.Staff_apply_leave,name='apply_leave'),
        path('staff/apply/leave/save',Staff_views.Staff_apply_leave_save,name='staff_apply_leave_save'),
        path('staff/take/attendence',Staff_views.Staff_take_attendence,name='staff_take_attendence'),
        
        
        path('staff/add/result',Staff_views.Staff_add_result,name='staff_add_result'),
        # path('staff/save/result',Staff_views.Staff_save_result,name='staff_save_result'),
        #this is student url
        path('student/home/', Student_views.Home, name='student_home'),  
         path('student/notification',Student_views.Student_notification_send,name='student_notification'),
           path('student/mark/done/<str:status>',Student_views.Student_notification_mark_as_done,
                name='student_notification_mark'),
            path('student/apply/leave',Student_views.Student_apply_leave,name='leave'),
             path('student/apply/leave/save',Student_views.Student_apply_leave_save,name='student_apply_leave_save'),
        
        
        
         
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
