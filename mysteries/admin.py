from django.contrib import admin
from .models import User, Mystery, Answer, Skill, Tag

# Register your models here.
admin.site.register(User)
admin.site.register(Mystery)
admin.site.register(Answer)
admin.site.register(Skill)
admin.site.register(Tag)