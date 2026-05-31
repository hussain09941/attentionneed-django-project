from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

class Service(models.Model):
    title = models.CharField(max_length=120)
    icon = models.CharField(max_length=50, default='bi bi-code-slash')
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=150)
    #image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField()
    technology_used = models.CharField(max_length=250)
    project_link = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
   # image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Admin')
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.client_name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='team/', blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    bio = models.TextField()
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username




#video model
class HeroVideo(models.Model):
    title = models.CharField(max_length=200)
    #video = models.FileField(upload_to='videos/')
    video = CloudinaryField(resource_type="video")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title