from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView,FilteredBloodView,FilteredHospitalView,FilteredCityView,DashboardView
)
from . import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView, name='post-detail'),
    path('dashboard/', views.DashboardView, name='dash-view'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('home/', views.home, name='main-home'),
    path('category/<str:cats>/', FilteredBloodView, name='category'),
    path('category1/<str:cats>/', FilteredHospitalView, name='category1'),
    path('category2/<str:cats>/', FilteredCityView, name='category2'),
    path('faq/', views.faq, name='faq'),
    path('news/', views.news, name='news'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)