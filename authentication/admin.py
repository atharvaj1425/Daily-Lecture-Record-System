from django.contrib import admin
from .models import Section, LectureRecord, CustomUser, FormData
from django.contrib.auth.admin import UserAdmin

admin.site.register(Section)

class LectureRecordAdmin(admin.ModelAdmin):
    list_display = ('lr_id', 'section', 'course_number', 'course_name', 'instructer_id', 'instructer_name', 'time', 'day')
    list_filter = ('section', 'course_number', 'instructer_id', 'time', 'day')
    search_fields = ('section__name', 'course_number', 'instructer_id', 'instructer_name')

# Register your model with the admin site
admin.site.register(LectureRecord, LectureRecordAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('UniqueId',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('UniqueId',),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class FormDataAdmin(admin.ModelAdmin):
    list_display = ('fd_id', 'section', 'course_number', 'course_name', 'time', 'day', 'assignment_given', 'assignment_collected', 'assignment_distributed', 'remarks', 'instructer_id', 'instructer_name', 'date')
    list_filter = ('section', 'course_number', 'instructer_id', 'time', 'day', 'date')
    search_fields = ('section', 'course_number', 'instructer_id', 'instructer_name', 'remarks')

# Register your model with the admin site
admin.site.register(FormData, FormDataAdmin)