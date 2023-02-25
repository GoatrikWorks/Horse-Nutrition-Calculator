from django.conf.urls import url
from django.urls import path
from AppTwo import views

#TEMPLATE TAGGING

app_name = 'AppTwo'

# urlpatterns = [
#     path('', views.help, name='help'),
# ]
urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    # path('relative', views.relative, name='relative'),
]
