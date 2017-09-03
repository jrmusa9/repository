from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', (views.index)),
    url(r'^register$', (views.register)),
    url(r'^login$', (views.login)),
    url(r'^quotes$', (views.quotes)),
    url(r'^remove/(?P<fav_id>\d+)$$', (views.remove)),
    url(r'^add$', (views.add)),
    url(r'^add_favorite/(?P<fav_id>\d+)$', (views.add_favorite)),
    url(r'^user/(?P<user_id>\d+)$', (views.user)),
    url(r'^logout$', (views.logout)),
    # url(r'^join/(?P<trip_id>\d+)$', (views.join)),
    # url(r'^destination/(?P<trip_id>\d+)$', (views.destination)),
]


