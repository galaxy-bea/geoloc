from django.contrib import admin
from .models import Marker
from .models import Category
from .models import SubCategory
# Register your models here.
admin.site.register(Marker)
admin.site.register(Category)
admin.site.register(SubCategory)
