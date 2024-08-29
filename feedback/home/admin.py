from django.contrib import admin
from .models import Questions, Options, CustomerFeedback, Response

admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(CustomerFeedback)
admin.site.register(Response)
