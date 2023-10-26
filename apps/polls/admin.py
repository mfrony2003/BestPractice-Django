from django.contrib import admin

# Register your mod
from apps.polls.models import Question,Answer

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
