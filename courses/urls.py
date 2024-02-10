from django.urls import path, include
from .views import CourseList, CourseDetail, CourseListAPIView, CourseDetailAPIView, CourseViewSet

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('courses-api/', CourseListAPIView.as_view(), name='courses-api'),
    path('courses-api/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail-api'),
    path('course-viewset/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-viewset'),
    path('course-viewset/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='course-viewset-detail')
]

