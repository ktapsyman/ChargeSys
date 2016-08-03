from django.conf.urls import url
from . import views
app_name='Hello'
urlpatterns = [
	url( r'^$', views.index, name="index" ),
	url( r'^Greeting/(?P<name>\w+)$', views.Greeting, name="Greetings" ),
	url( r'^TestPost/$', views.TestPostWithJson, name="TestPost" ),
]
