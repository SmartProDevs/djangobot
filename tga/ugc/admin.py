from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(New)

