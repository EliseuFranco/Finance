from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Register(AbstractUser):
    first_name = models.CharField(max_length=200, blank=True, null=True, default='Hello')
    last_name = models.CharField(max_length=200, blank=True, null=True, default='World')

    def __str__(self):
            return f"{self.first_name} {self.last_name}"


class Expenses(models.Model):
    ID_expense = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=100, default='Unnamed Expense')
    expense_value = models.FloatField(blank=False, null=False)
    category = models.CharField(max_length=100, default='Miscellaneous')
    date = models.DateField(blank=False, null=False, default=timezone.now)
    choose = models.CharField(max_length=100, default='Expense')
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='expenses')
    amount_earn = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self):
        return f"{self.expense_name} - {self.user.get_full_name()}"
