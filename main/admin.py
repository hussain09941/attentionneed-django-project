from django.contrib import admin
from .models import Service, Project, BlogPost, ContactMessage, Testimonial, TeamMember, UserProfile,HeroVideo

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology_used', 'created_at')
    search_fields = ('title', 'technology_used')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category', 'author')
    list_filter = ('category', 'created_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_read', 'created_at')

admin.site.register(Testimonial)
admin.site.register(TeamMember)
admin.site.register(UserProfile)

admin.site.site_header = 'Attentionneed Admin'
admin.site.site_title = 'Attentionneed Admin'
admin.site.index_title = 'Website Management'

admin.site.register(HeroVideo)