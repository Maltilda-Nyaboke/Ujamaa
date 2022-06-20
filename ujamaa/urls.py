from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include


urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('update_profile/',views.update_profile, name='update_profile'),
    path('search/',views.search, name='search'),
    path('join/<int:id>/',views.join_hood, name='join'),
    path('leave/',views.leave_hood, name='leave'),
    path ('neighborhood/<int:id>',views.neighborhood, name='neighborhood'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
