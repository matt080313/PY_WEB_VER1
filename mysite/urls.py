"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from mysite.views import IndexView
from bookmark.views import BookmarkLV, BookmarkDV
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings
from mysite.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreationView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreationDoneTV.as_view(), name='register_done'),




    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^bookmark/$', BookmarkLV.as_view(), name='bookmark_index'),   #http://127.0.0.1:8000/bookmark
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name="detail"),


    url(r'^blog/$', PostLV.as_view(),
        name='blog_index'),

    url(r'^blog/add/$', PostCreateView.as_view(), name="blog_add"),

    url(r'^blog/(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="blog_delete"),

    url(r'^blog/(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="blog_update"),

    url(r'^elemental_battleground/$', GameTips_Elemental_Battleground_View.as_view(), name="elemental_battleground"),

    url(r'^factory_town_tycoon/$', GameTips_Factory_Town_Tycoon_View.as_view(), name="factory_town_tycoon"),

    url(r'^resource_factory_tycoon/$', GameTips_Resource_Factory_Tycoon_View.as_view(), name="resource_factory_tycoon"),

    url(r'^restaurant_tycoon_2/$', GameTips_Restaurant_Tycoon_2_View.as_view(), name="restaurant_tycoon_2"),

    url(r'^critical_strike/$', GameTips_Critical_Strike_View.as_view(), name="critical_strike"),

    url(r'^lua_coding_on_roblox/$', Lua_Coding_On_Roblox_View.as_view(), name="lua_coding"),

    url(r'^blog/change/$', PostChangeLV.as_view(), name='blog_change_list'),


    url(r'^blog/(?P<pk>\d+)/$', PostDV.as_view(), name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
