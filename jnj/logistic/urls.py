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

    url(r'^get_price_rent/$', views.get_price_rent, name='get_price_rent'),
    url(r'^get_price_rent_step_1/(?P<cargo_type_id>[0-9]+)/$', views.get_price_rent_step_1, name='get_price_rent_step_1'),

    # generic will show under constructions
    url(r'^get_price_rent_step_2/(?P<cargo_type_id>[0-9]+)/(?P<transport_service_id>[0-9]+)/$', views.get_price_rent_step_2, name='get_price_rent_step_2'),
    url(r'^get_price_rent_step_3/(?P<cargo_type_id>[0-9]+)/(?P<transport_service_id>[0-9]+)/(?P<transport_id>[0-9]+)/$', views.get_price_rent_step_3, name='get_price_rent_step_3'),
    url(r'^calculate_rent_price/$', views.calculate_rent_price, name='calculate_rent_price'),

    # domestic delivery
    url(r'^get_price_rent_step_2_domestic/(?P<cargo_type_id>[0-9]+)/(?P<transport_service_id>[0-9]+)/$', views.get_price_rent_step_2_domestic, name='get_price_rent_step_2_domestic'),
    url(r'^get_price_rent_step_3_domestic/(?P<cargo_type_id>[0-9]+)/(?P<transport_service_id>[0-9]+)/(?P<transport_id>[0-9]+)/$', views.get_price_rent_step_3_domestic, name='get_price_rent_step_3_domestic'),
    url(r'^calculate_price_rent_domestic/$', views.calculate_price_rent_domestic, name='calculate_price_rent_domestic'),

    url(r'^get_price_package/$', views.get_price_package, name='get_price_package'),
    url(r'^calculate_price_package/$', views.calculate_price_package, name='calculate_price_package'),

]
