from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('feedback/<int:id>/', CustomerFeedback, name="CustomerFeedback"),  # Use <int:id> to specify that 'id' is an integer
]
