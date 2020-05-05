from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^userlist/$', views.UserProfileView.as_view(), name='userlist'),
    url(r'^user/show/(?P<pk>\w+)$', views.UserDetailView.as_view(), name='user-detail'),

    url(r'^user/add/$', views.add_user, name='add-user'),

    url(r'^shop/$', views.ShopItemsViewList.as_view(), name='shop'),
    url(r'^shop/bucket/$', views.shop_bucket, name='shop-bucket'),

]
