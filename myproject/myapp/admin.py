from django.contrib import admin

# Register your models here.
from .models import UserInfo, Questions, FAQ, Calorie

admin.site.register(UserInfo)
admin.site.register(Questions)
admin.site.register(FAQ)
admin.site.register(Calorie)