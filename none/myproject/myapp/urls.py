from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('add_item/', views.add_item, name='add_item'),
    path('list_items/', views.list_items, name='list_items'),
    path('inventory/', views.inventory, name='inventory'),
    path('login/', views.login_view, name='login'),
    path('accounts/profile/', views.profile_view, name='profile'),
]
