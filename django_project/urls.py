from django.contrib import admin
from django.urls import path, include
from appSW import views, forms

urlpatterns = [
    path('accounts/register/', views.register_user, name='register'),
    path('accounts/confirm_logout/', views.confirm_logout, name="confirm_logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.homePage,name="homePage"), 
    path('sequelsPros/',views.sequelsProsPage,name="sequelsProsPage"),
    path('sequelsPros/add/',views.add_sequelsPros,name="add_sequelsPros"),
    path('sequelsPros/update/<int:sequelsPros_id>/',views.update_sequelsPros,name="update_sequelsPros"),
    path('sequelsPros/delete/<int:sequelsPros_id>/',views.delete_sequelsPros,name="del_sequelsPros"),
    path('chapters/',views.chaptersPage,name="chaptersPage"),
    path('chapters/add/',views.add_chapters,name="add_chapters"),
    path('chapters/update/<int:chapters_id>/',views.update_chapters,name="update_chapters"),
    path('chapters/delete/<int:chapters_id>/',views.delete_chapters,name="del_chapters"),
    path('admin/', admin.site.urls), 
]
