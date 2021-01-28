from django.contrib import admin
from . models import Alphabet,Alphanumeric,Numeric

# Register your models here.
admin.site.register(Alphabet)
admin.site.register(Alphanumeric)
admin.site.register(Numeric)
