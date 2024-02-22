from django.urls import path
from .import views 
urlpatterns = [

    path('sucessful/', views.sucessful, name ='sjdba'),
    path('created/', views.created),
    path('accepted/', views.accepted),
    path('non-authorization/', views.non_authorization),
    path('found', views.found),
    path('bad-request/', views.bad_request),
    # path('unauthorized/', views.unauthorized),
    # path('payment-required/', views.payment_required),
    # path('forbidden/', views.forbidden),
    # path('not-found/', views.not_found),
    # path('request-timeout/', views.request_timeout),
    # path('conflict/', views.conflict),
    # path('url-too-long/', views.url_too_long),
    # path('internal-server-error/', views.internal_server_error),
    # path('bad-gateway/', views.bad_gateway),
    # path('service-unavailable/', views.service_unavailable),
    # path('http-version-not-supported/', views.http_version_not_supported),
    # path('loop-detected/', views.loop_detected),

    
]
