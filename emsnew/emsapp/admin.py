from django.contrib import admin

# Register your models here.

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')

admin.site.register(Contact,ContactAdmin)

from .models import Query

class QueryAdmin(admin.ModelAdmin):
    list_display = ('name','query')

admin.site.register(Query,QueryAdmin)




from .models import AdminLogin

class AdminLoginAdmin(admin.ModelAdmin):
    list_display = ('name','password')

admin.site.register(AdminLogin,AdminLoginAdmin)

from .models import EmployeeLogin

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','password')

admin.site.register(EmployeeLogin,EmployeeAdmin)