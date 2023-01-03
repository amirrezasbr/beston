from django.contrib import admin
from .models import Exopense, Income, Token
# Register your models here.


admin.site.register(Exopense)
admin.site.register(Income)
admin.site.register(Token)