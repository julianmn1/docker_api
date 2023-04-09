from django.contrib import admin
from django.urls import path, include

from test_app.views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TestView.as_view()),
]
