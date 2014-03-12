127#-*- coding: utf-8 -*-
from app.models import MyUser
from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display   = ('id','username','first_name','last_name','nbPoke','email','is_active','is_superuser','is_staff','last_login','password')
    list_filter    = ('is_active',)
    ordering       = ('id', )
    search_fields  = ('username', 'first_name','last_name','email')

#admin.site.unregister(User)
admin.site.register(MyUser,UserAdmin)