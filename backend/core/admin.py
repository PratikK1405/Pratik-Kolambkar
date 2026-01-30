from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, Project, ProjectImage, TechStack,
    Skill, Experience, Education, ContactMessage
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'order', 'image_preview']
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 200px;" />',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Preview'


class TechStackInline(admin.TabularInline):
    model = TechStack
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'available_for_work', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'role', 'tagline', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'dribbble_url')
        }),
        ('Additional Info', {
            'fields': ('resume', 'available_for_work', 'years_experience', 'projects_completed')
        }),
    )
    
    def has_add_permission(self, request):
        # Prevent adding more than one profile
        return not Profile.objects.exists()


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_at']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description']
    list_editable = ['featured', 'order']
    inlines = [ProjectImageInline, TechStackInline]
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'category', 'featured', 'order')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    search_fields = ['name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'duration', 'order']
    list_editable = ['order']
    search_fields = ['title', 'organization']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'duration', 'order']
    list_editable = ['order']
    search_fields = ['title', 'organization']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    list_editable = ['read']
    
    def has_add_permission(self, request):
        return False


# Customize admin site
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"