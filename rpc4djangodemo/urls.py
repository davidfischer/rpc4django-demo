from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'rpc4django.views.serve_rpc_request'),
    (r'^RPC2$', 'rpc4django.views.serve_rpc_request'),
)
