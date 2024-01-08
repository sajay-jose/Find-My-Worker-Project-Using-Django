from django.contrib import admin
from .models import CustomUser, Job, JobApplications, JobCategory

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobApplications)
