from django.conf.urls import url

from . import views

app_name = 'logistic'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^notifications/$', views.notifications_user, name='notifications_user'),
    url(r'^notifications/(?P<notification_id>[0-9]+)/$', views.notifications_user_detail, name='notifications_user_detail'),

    url(r'^products_and_services/$', views.products_and_services, name='products_and_services'),


    url(r'^check_shipment/$', views.check_shipment, name='check_shipment'),
    url(r'^get_price/$', views.get_price, name='get_price'),
    url(r'^get_price_step_1/(?P<cargo_type_id>[0-9]+)/$', views.get_price_step_1, name='get_price_step_1'),
    url(r'^get_price_step_2/(?P<cargo_type_id>[0-9]+)/(?P<transport_service_id>[0-9]+)/$', views.get_price_step_2, name='get_price_step_2'),
    url(r'^get_price_step_3/(?P<cargo_type_id>[0-9]+)/(?P<transport_service_id>[0-9]+)/(?P<transport_id>[0-9]+)/$', views.get_price_step_3, name='get_price_step_3'),
]
