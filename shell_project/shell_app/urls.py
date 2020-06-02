from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import Shell

app_name = 'shell_app'

urlpatterns = [
    path('', staff_member_required(Shell.as_view()), name='shell'),
]