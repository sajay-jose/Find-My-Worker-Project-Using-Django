"""
URL configuration for Find_My_Worker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name='about'),
    path('jobs', views.jobs, name="jobs"),
    path('job_details', views.job_details, name="job_details"),
    path('contact', views.contact, name="contact"),
    path('Worker_register', views.worker_register, name="Worker_register"),
    path('employer_register', views.employer_register, name="employer_register"),
    path('Login', views.Login, name="Login"),
    path('Logout',views.Logout, name="Logout"),
    path('view_jobs',views.view_jobs, name="view_jobs"),

    #############################################################################
    path('Worker_home', views.worker_home, name="Worker_home"),
    path('Worker_profile', views.worker_profile, name="Worker_profile"),
    path('worker_history', views.worker_history, name="worker_history"),
    path('job_apply/<int:id>', views.job_apply, name="job_apply"),
    path('worker_edit_profile', views.worker_edit_profile,name="worker_edit_profile"),

    path('employer_home', views.employer_home, name="employer_home"),
    path('employer_profile', views.employer_profile, name="employer_profile"),
    path('employer_edit_profile', views.employer_edit_profile, name="employer_edit_profile"),
    path('add_jobs', views.add_jobs, name="add_jobs"),
    path('edit_job/<int:id>', views.edit_job, name="edit_job"),
    path('delete_job/<int:id>', views.delete_job, name="delete_job"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
