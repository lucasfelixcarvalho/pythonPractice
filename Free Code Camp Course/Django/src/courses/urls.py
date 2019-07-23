from django.urls import path
from .views import (
    CourseDeleteView,
    CourseListView,
    CourseUpdateView,
    CourseView,
    CourseCreateView
)
app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(template_name='courses/courses.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(template_name='courses/courses_detail.html'), name='courses-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(template_name='courses/courses_update.html'), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(template_name='courses/courses_delete.html'), name='courses-delete'),
    path('create/', CourseCreateView.as_view(template_name='courses/courses_create.html'), name='courses-create'),
]