from app.views import UserCreate, UserDetail
from app.decorators import logout_required
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('app.views',
    url(r'^$', 'home', name='home'),
    url(r'^login/$', 'connexion', name='connexion'),
    url(r'^logout/$', 'deconnexion', name='deconnexion'),
    url(r'^poke/(?P<username>\w+)/$', 'poke', name='poke'),
    url(r'^user/(?P<pk>\d+)/$', login_required(UserDetail.as_view()), name='user'),
    url(r'^suscribe/$', UserCreate.as_view(), name='suscribe'),
)
