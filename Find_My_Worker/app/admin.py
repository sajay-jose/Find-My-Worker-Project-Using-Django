from django.contrib import admin
from .models import CustomUser, Job, JobApplications, JobCategory

# Register your models here.

class UserDetails(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["username", "user_type"]}),
        ("More information", {"fields": ["phone_number", "email"]}),
    ]

    list_display = ["username", "user_type"]    
    list_filter = ["user_type", ]                           #filtering
    search_fields = ["username"]                                    #search
    list_per_page = 10 



admin.site.register(CustomUser, UserDetails)
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobApplications)
