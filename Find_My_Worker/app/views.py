from django.shortcuts import render,redirect
from .models import CustomUser,Job,  JobApplications,JobCategory
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .forms import WorkerEditForm, EmployerEditForm

# Create your views here.

def home(request):
    jobs = JobCategory.objects.all()
    return render(request, 'Home/index.html', {'jobs': jobs})


def about(request):
    return render(request, 'Home/about.html')

def jobs(request):
    jobs = JobCategory.objects.all()
    return render(request, 'Home/jobs.html', {'jobs':jobs})

def job_details(request):
    return render(request, 'Home/job-details.html')

def contact(request):
    return render(request, 'Home/contact.html')

def worker_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        description = request.POST['about_me']
        pic = request.FILES['image']
        data = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            email=email,
            description=description,
            pic=pic,
            username=username,
            password=password,
            user_type=1
        )
        data.save()
        return redirect(Login)

    else:    
        return render(request, 'Home/worker-register.html')

def employer_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        description = request.POST['about_me']
        pic = request.FILES['image']
        data = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            email=email,
            description=description,
            pic=pic,
            username=username,
            password=password,
            user_type=0
        )
        data.save()
        return redirect(Login)
    else:    
        return render (request, 'Home/employer-register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
         # Authenticate superusers (admins)
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request, admin_user)
            return redirect(reverse('admin:index'))  # Redirect to the admin dashboard
        elif user is not None:
            # If not an admin, check regular users            
            login(request, user)
            if user.user_type == 1:     #worker profile
                return redirect(worker_home)
            elif user.user_type == 0:   #Employer profile
                return redirect(employer_home)  
        else:
            context = {
                'message': "*Invalid credentials"
            }
            return render(request, 'Home/login.html', context)
    else:
        return render(request, 'Home/login.html')
    
def Logout(request):
    logout(request)
    return redirect(Login)







def worker_home(request):
    data = CustomUser.objects.get(id=request.user.id)
    jobs = Job.objects.all()

    context = {
        'user': data,
        'jobs':jobs
    }
    return render(request, 'Worker/worker-home.html', context)

def worker_profile(request):
    data = CustomUser.objects.get(id=request.user.id)
    print(data)
    context = {
        'user': data
    }
    return render(request, 'Worker/profile.html', context)

def worker_edit_profile(request):
    User = CustomUser.objects.get(id = request.user.id) 
    form = WorkerEditForm(instance=User)
    if request.method == 'POST':
        form = WorkerEditForm(request.POST, instance=User)
        if form.is_valid():
            form.save()
            return redirect(worker_profile)
        else:
            context = {
                'message': "Please enter valid data"
            }
            return render(request, 'Worker/edit-profile.html', context)
    else:
         return render(request, 'Worker/edit-profile.html',{'form':form})

def view_jobs(request):
    jobs = Job.objects.all()
    print(jobs)
    return render(request, 'Worker/jobs.html', {'jobs':jobs})

def search_jobs(request):
    User = CustomUser.objects.get(id=request.user.id)
    if request.method == 'GET':
        search_query = request.GET.get('search')
        if search_query:
            jobs = Job.objects.filter(jobcategory_id__job_name__icontains=search_query)
            return render(request, 'Worker/jobs.html', {'jobs':jobs, 'User':User})

def job_apply(request,id):
    worker = CustomUser.objects.get(id=request.user.id)
    job = Job.objects.get(id=id)
    JobApplications.objects.create(worker_id=worker,job_id=job)
    return redirect(view_jobs)



def worker_history(request):
    worker = CustomUser.objects.get(id=request.user.id)
    applications = JobApplications.objects.filter(worker_id=worker)
    print(applications)
    return render(request, 'Worker/history.html', {'applications':applications})


###############################################################################################################





def employer_profile(request):
    data = CustomUser.objects.get(id=request.user.id)
    print(data)
    context = {
        'user': data
    }
    return render(request, 'Employer/profile.html', context)

def employer_edit_profile(request):
    User = CustomUser.objects.get(id = request.user.id) 
    if request.method == 'POST':
        User.first_name = request.POST['first_name']
        User.last_name = request.POST['last_name']
        User.address = request.POST['address']
        User.phone_number = request.POST['contact']
        User.email = request.POST['email']
        User.username = request.POST['username']
        User.description = request.POST['about_me']
        User.pic = request.FILES['image']
        User.save()
        return redirect(employer_profile)
    else:
         context = {
             'User':User
         }
         return render(request, 'Employer/edit-profile.html', context)



def employer_home(request):
    employer = CustomUser.objects.get(id=request.user.id)
    jobs = Job.objects.filter(employer_id=employer)
    print(jobs)
    context = {
        'employer':employer,
        'jobs':jobs,
        }
    return render(request, 'Employer/employer-home.html', context)


def add_jobs(request):
    employer = CustomUser.objects.get(id=request.user.id)
    jobcategory = JobCategory.objects.all()
    jobs = Job.objects.filter(employer_id=employer)
    if request.method == 'POST':
        JOBcategory_id = request.POST['jobcategory']
        price = request.POST['price']
        description = request.POST['description']
        jobcategory_id = JobCategory.objects.get(id=JOBcategory_id)
        job = Job.objects.create(employer_id=employer, jobcategory_id=jobcategory_id, Price=price, description=description)
        job.save()
        return redirect(employer_home)

    else:
        context = {
        'employer':employer,
        'jobs':jobs,
        'jobcategory':jobcategory
        }
    return render(request, 'Employer/employer-home.html', context)
    
def edit_job(request,id):
    jobs = Job.objects.get(id=id)
    print(jobs)
    if request.method == 'POST':
        jobs.Price = request.POST['price']
        jobs.description = request.POST['description']
        jobs.save()
        return redirect(employer_home)
    context = {
        'jobs':jobs,
        }
    return render(request, 'Employer/edit_job.html', context)

def delete_job(request,id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect(employer_home)

def employer_application(request):
    employer = CustomUser.objects.get(id=request.user.id)

    