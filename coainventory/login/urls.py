from django.conf.urls import url, patterns, include
from views import login, auth_view, invalid_login, logout

urlpatterns = [
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/auth/$', auth_view, name="auth_view"),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/invalid/$', invalid_login, name='invalidlogin'),

]