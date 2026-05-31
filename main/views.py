from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Service, Project, BlogPost, Testimonial, TeamMember, ContactMessage, UserProfile,HeroVideo
from .forms import ContactForm, SignupForm

# def home(request):
#     services = Service.objects.filter(is_active=True)[:6]
#     projects = Project.objects.all()[:3]
#     testimonials = Testimonial.objects.all()[:3]
#     return render(request, 'main/home.html', {'services': services, 'projects': projects, 'testimonials': testimonials})


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    projects = Project.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]

    # Get latest uploaded video
    video = HeroVideo.objects.last()

    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'video': video,
    }

    return render(request, 'main/home.html', context)

def about(request):
    team = TeamMember.objects.all()
    return render(request, 'main/about.html', {'team': team})

def services(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'main/services.html', {'services': services})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'main/blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'main/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            if request.user.is_authenticated:
                msg.user = request.user
            msg.save()
            messages.success(request, 'Your message has been submitted successfully.')
            return redirect('contact')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            UserProfile.objects.create(user=user, phone=form.cleaned_data.get('phone',''), company=form.cleaned_data.get('company',''))
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    messages_list = ContactMessage.objects.filter(user=request.user)
    return render(request, 'main/dashboard.html', {'messages_list': messages_list})
