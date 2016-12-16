"""survey_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from survey_api_app import views

urlpatterns = [
	url(r'^api/(?P<age_range>\w{0,50})/(?P<family_monthly_income>\w{0,50})',views.get_mobile_brands,name='get_mobile_brands'),
	url(r'^count/(?P<age_range>\w{0,50})/(?P<family_monthly_income>\w{0,50})',views.get_mobile_brands_counts,name='get_mobile_brands_counts'),
    url(r'^admin/', admin.site.urls),
]
