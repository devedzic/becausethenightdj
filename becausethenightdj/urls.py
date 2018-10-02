"""becausethenightdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


# Added automatically when the project is created initially.
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Include music.urls as soon as music\urls.py is created in the music package.
urlpatterns += [
    path('music/', include('music.urls')),
]

# Add URL maps to redirect the base URL to the music app, i.e. make 'music/' the landing page.
urlpatterns += [
    path('', RedirectView.as_view(url='music/'))
]

# Enable serving of static files during development.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




