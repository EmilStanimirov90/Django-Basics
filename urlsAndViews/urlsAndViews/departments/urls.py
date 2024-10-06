from django.urls import path, re_path, include

from urlsAndViews.departments import views


urlpatterns = [
    path('', views.index, name='home'),
    path('redirect-to-view/', views.redirect_to_view, name = 'redirect-to-view'),
    path('softuni/', views.redirect_to_softuni),
    path('<variable>/',views.view_with_name),
    path('numbers/', include([
        path('<int:pk>/',views.view_with_int_pk),
        path('<slug:slug>/', views.view_with_slug),
    ])),

    re_path(r'^archive/(?P<year>202[0-3])/$', views.show_archive),
    path('<path:variable>/',views.view_with_name),
    # path('<uuid:id>', some_view)

]