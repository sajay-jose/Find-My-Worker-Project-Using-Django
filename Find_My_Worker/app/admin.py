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


class JobDetails(admin.ModelAdmin):
    list_display = ["user_username", "get_jobcategory_name", "Price"]
    list_filter = ["Price"]
    search_fields = ["user_id__username", "jobcategory_id__job_name"]  # Update to use jobcategory_id__job_name
    list_per_page = 10

    # Define a method to get related fields
    def user_username(self, obj):
        return obj.user_id.username
    
    def get_jobcategory_name(self, obj):
        return obj.jobcategory_id.job_name


    # Customize the column headers
    user_username.short_description = "Username"
    get_jobcategory_name.short_description = "Job Category"

class BookingDetails(admin.ModelAdmin):
    list_display = ["user_username", "package_name", "status"]
    list_filter = ["status"]
    search_fields = ["user_id__username", "package_id__package_name"]  # Update to use user_id__username
    list_per_page = 10

    # Define a method to get related fields
    def user_username(self, obj):
        return obj.user_id.username

    def package_name(self, obj):
        return obj.package_id.package_name

    # Customize the column headers
    user_username.short_description = "Username"
    package_name.short_description = "Package Name"


admin.site.register(CustomUser, UserDetails)
admin.site.register(Job, JobDetails)
admin.site.register(JobCategory)
admin.site.register(JobApplications)
