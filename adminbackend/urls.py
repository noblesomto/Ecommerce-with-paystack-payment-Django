from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('adminbackend/register', views.register, name='register'),
    path('adminbackend/login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('adminbackend/dashboard', views.dashboard, name='dashboard'),
    path('adminbackend/all-post', views.all_post, name='all-post'),
    path('adminbackend/new-post', views.new_post, name='new_post'),
    path('post_details/<str:id>', views.post_details, name='post_details'),
    path('adminbackend/edit-post/<str:id>', views.edit_post, name='edit-post'),
    path('adminbackend/delete-post/<str:id>',
         views.delete_post, name='delete-post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
