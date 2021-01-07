from django.contrib import admin
from .models import srs, raw_score, t_score, students
# Register your models here.

admin.site.register(srs)
admin.site.register(raw_score)
admin.site.register(t_score)
admin.site.register(students)
