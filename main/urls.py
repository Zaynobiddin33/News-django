from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allnews/',  views.allnews, name='allnews'),
    path('category/',  views.category, name='category'),
    path('contact/',  views.contact, name='contact'),
    path('details/',  views.details, name='details'),
    # dashboard
    path('dashboard', views.dashboard, name='dash'),
    # dashboard region
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    # dashboard category
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/categories/list', views.categories, name = 'categories'),
    path('dashboard/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashboard/category/delete/<int:id>/', views.category_delete, name='category_delete'),
    # dashboard news
    path('dashboard/news/create', views.create_item, name='create_item'),
    path('dashboard/news/list', views.items, name='items'),
    path('dashboard/news/update/<int:id>/', views.update_item, name='update_item'),
    path('dashboard/news/delete/<int:id>/', views.delete_item, name='delete_item'),
    #messages
    path('dashboard/message/list', views.messages, name='messages'),
    path('dashboard/message/update/<int:id>/', views.update_status, name='update_status'),


    
]