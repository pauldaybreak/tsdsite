from django.conf.urls import url
from . import views
from .views import *
from django_filters.views import FilterView

urlpatterns = [
	
	url(r'^$', index, name='index'),
	url(r'^display_devices$', display_devices, name='display_devices'),
	url(r'^display_tsd$', display_tsd, name='display_tsd'),
	url(r'^display_techniks$', display_techniks, name='display_techniks'),
	url(r'^add_device$', add_device, name='add_device'),
	url(r'^login_page$', login_page, name='login_page'),
	url(r'^logout$', logout_user, name = "logout_user"),
	url(r'^display_repair$', display_repair, name='display_repair'),
	url(r'^add_repair$', add_repair, name='add_repair'),

	url(r'^edit_device/(?P<pk>\d+)$', edit_device, name='edit_device'),

	url(r'^edit_repair/(?P<pk>\d+)$', edit_repair, name='edit_repair'),
	url(r'^registerPage$', registerPage, name='registerPage'),
	url(r'^go_to_remont/(?P<pk>\d+)$', go_to_remont, name='go_to_remont'),
	url(r'^export_excel$', export_excel, name='export_excel'),
	url(r'^search/$', FilterView.as_view(filterset_class=WarehouseDeviceFilter, template_name='whdevice_filter.html'), name='search'),

	#url(r'^export_csv$', export_csv, name='export_csv')
	#url(r'^from_remont/(?P<pk>\d+)$', from_remont, name='from_remont')
	
]