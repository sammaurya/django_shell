from django.urls import path
from .views import Shell

app_name = 'shell_app'

urlpatterns = [
    path('', Shell.as_view(), name='shell'),
]