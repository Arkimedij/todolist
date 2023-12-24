from django.contrib import admin
from django.urls import path
from todoapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('task/',views.task,name = 'task'),
    path('delete/',views.delete, name = 'delete')
    path('edit/',views.edit_task, name = 'edit')
]
