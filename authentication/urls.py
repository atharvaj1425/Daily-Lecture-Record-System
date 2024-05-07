from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('dynamic_page', views.dynamic_page,name="dynamic_page"),
    path('signout', views.signout, name="signout"),
    path('dlr',views.dlr,name="daily_lecture_record"), 
    path('dlr_history',views.dlr_history,name="dlr_history"),
    path('testdlr/<int:dlr_id>/', views.testdlr_detail, name='testdlrdetail'),
    path('updatedlr/<int:dlr_id>/', views.updatedlr_detail, name='updatedlrdetail'),
    path('save-form-data/<int:fd_id>/', views.save_form_data, name='save_form_data'),
    path('update-form-data/<int:fd_id>/', views.update_form_data, name='update_form_data'),
    path('view_dlr', views.view_dlr, name='view_dlr'),
    path('faculty_tt', views.faculty_tt, name="faculty_tt"),
    # path('hod', views.hod, name="hoddash"),
    # path('admin', views.admin, name="admindash"),
    # path('faculty', views.faculty, name="facultydash"),
    #path('admin_dlr',views.admin_dlr,name="admin_dlr"),
    #path('signup', views.signup, name="signup"),
]