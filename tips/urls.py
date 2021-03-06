from django.conf.urls import url

from . import views

app_name = 'tips'
urlpatterns = [
	url(r'^$', views.all_tip_list, name="all-tips"),
	url(r'^series/$', views.all_series_list, name="series"),
	url(r'^tips/', views.all_tip_list, name="tips"),
	url(r'^series/(?P<pk>[0-9]+)/', views.all_tips_in_series, name='series_detail'),
	url(r'^likes/', views.like, name='like'),
	url(r'^dislikes/', views.dislike, name='dislikes'),
	url(r'^sort-resources/', views.sort_resources, name='sort-resources'),
]