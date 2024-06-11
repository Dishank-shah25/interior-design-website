from .import views
from django.urls import path
urlpatterns = [
    path('service.html',views.service,name='service.html'),
    path('service-details.html',views.servicedetails,name='service-details.html'),
    path('service-details-2.html',views.servicedetails2,name='service-details-2.html'),
    # path('',views.index,name='index.html'),
    # path('category.html',views.blog,name='category.html'),
    path('blog-details.html',views.blogdetails,name='blog-details.html'),
    path('contact.html',views.contact,name='contact.html'),
    path('about.html',views.about,name='about.html'),
    path('fetchformdata',views.fetchformdata,name='fetchformdata'),
    path('fetchdata',views.fetchdata,name='fetchdata'),
    path('hello',views.hello,name='hello'),
    path('',views.newimage,name='newimage'),
    path('index.html',views.newimage,name='newimage'),
    path('category.html',views.category,name='blogfunction'),
    path('gallery.html',views.secondgalleryimg,name='secondgalleryimg'),
    path('products.html', views.products, name='products.html'),
    path('shopcategory.html',views.scategory,name='shopcategory.html'),
    path('shop-details.html',views.shop_details,name='shop-details.html'),
    path('login.html',views.login,name='login.html'),
    path('shop.html',views.shop,name='shop.html'),
]