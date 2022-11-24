from django.contrib import admin
from .models import Users,Client,Project
# Register your models here.

@admin.register(Project)
class display(admin.ModelAdmin):
    list_display=['project_name','users_info']

admin.site.register(Users)
admin.site.register(Client)

