from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import (
    signin, signup,
    profile, signout
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('signout/', signout, name='signout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
