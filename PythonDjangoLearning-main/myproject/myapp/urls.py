from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('render_view', render_view, name='render_view'),
    path('student_form', student_form, name='student_form'),
]