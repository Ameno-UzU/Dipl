from django.urls import path
from .views import *

urlpatterns = [
    path('', tasks, name='tasks'),
    path('home/', home, name='home'),
    path('tasks/',  tasks, name='tasks'),
    path('tools/',  tools, name='tools'),
    path('workers/',  workers, name='workers'),
    path('prof/<int:prof_id>/', show_prof, name='prof'),

]