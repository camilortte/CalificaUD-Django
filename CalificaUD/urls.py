from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Principal.views.index_general', name='home'),
    # url(r'^CalificaUD/', include('CalificaUD.foo.urls')),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'Principal.views.index_general',name='index_general'),
    url(r'^home/', 'Principal.views.index_private',name='index_private'),
    url(r'^login/', 'Principal.views.login',name='login'),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^logout/$', 'Principal.views.logout',name='logout'),	 
    #url(r'^registro/$', 'Principal.views.registration',name='registro'),   
    url(r'^profesores/', 'Principal.views.todos_los_profesores',name='todos_profesores'),   
    url(r'^registro/$', 'Principal.views.registration',name='registro'),   
    url(r'^actualizar/','Principal.views.actualizar',name='actualizar'),
    url(r'^cambiopassword/','Principal.views.change_password',name='change_password'),
    url(r'^calificar/','Principal.views.calificar',name='calificar'),
)
