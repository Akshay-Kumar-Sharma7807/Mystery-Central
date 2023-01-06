from django.contrib import admin
from .models import User, Mystery, Answer, Skill

# Register your models here.
admin.site.register(User)
admin.site.register(Mystery)
admin.site.register(Answer)
admin.site.register(Skill)