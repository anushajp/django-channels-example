from django.conf.urls import  include, url
from account.views import home, login, logout_view
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^login/', login),
    url(r'^accounts/login/', home),
    url(r'^logout/', logout_view),
    # url(r'^chat_home/', chat),
    # url(r'^chat/(?P<username>[^/]+)/$', individual_chat),
]