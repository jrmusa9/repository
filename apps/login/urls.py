from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', (views.index)),
    url(r'^register$', (views.register)),
    url(r'^login$', (views.login)),
    url(r'^travels$', (views.travels)),
    url(r'^adding$', (views.add)),
    url(r'^add_trip$', (views.add_trip)),
    url(r'^logout$', (views.logout)),
    url(r'^join/(?P<trip_id>\d+)$', (views.join)),
    url(r'^destination/(?P<trip_id>\d+)$', (views.destination)),
]
