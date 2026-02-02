from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r'posts', api_views.PostViewSet)
router.register(r'categories', api_views.CategoryViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<int:id>/', views.category_posts, name='category_posts'),
    path('api/', include(router.urls)),
]