from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    (r'^articles/',include('article.urls')),
    url(r'^static/(?P<path>.*)$', 'serve'),
	#url(r'^hello/$','article.views.hello'),
	#url(r'^hello_template/$','article.views.hello_template'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello_class_views/$',HelloTemplate.as_view()),
    
    url(r'^accounts/login/$','django_test.views.login'),
    url(r'^accounts/auth/$','django_test.views.auth_view'),
    url(r'^accounts/logout/$','django_test.views.logout'),
    url(r'^accounts/loggedin/$','django_test.views.loggedin'),
    url(r'^accounts/invalid/$','django_test.views.invalid_login'),
)
