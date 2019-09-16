from django.contrib import admin
from django.urls import path
from webapp.views import index_view, plan_view, plan_create_view, plan_edit, delete_view, item_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('plan/<int:pk>/', plan_view, name='view_plan'),
    path('plan/create/', plan_create_view, name='create_plan'),
    path('plan/<int:pk>/edit/', plan_edit, name='edit_plan'),
    path('plan/delete/<int:pk>/', delete_view, name='delete_plan'),
    path('plan/delete/item/', item_delete, name='delete_item'),
]
