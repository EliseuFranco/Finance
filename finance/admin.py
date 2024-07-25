from django.contrib import admin
from finance.models import Expenses, Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = (['first_name','last_name','email','password'])
    search_fields = (['name','surname'])

class ExpensesAdmin(admin.ModelAdmin):
    list_display = (['expense_name','expense_value','category','date','user'])
    search_fields = (['expesne_name'])

admin.site.register(Register, RegisterAdmin)
admin.site.register(Expenses, ExpensesAdmin)