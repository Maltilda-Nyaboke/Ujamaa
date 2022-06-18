from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include


urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
