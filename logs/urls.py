from django.urls import path

from logs.apps import LogsConfig
from logs.views import LogCreateAPIView, LogListAPIView, LogRetrieveAPIView, LogUpdateAPIView, LogDestroyAPIView, \
    LogSearchListAPIView

app_name = LogsConfig.name

urlpatterns = [
    path('create/', LogCreateAPIView.as_view(), name='log_create'),
    path('', LogListAPIView.as_view(), name='log_list'),
    path('view/<int:pk>', LogRetrieveAPIView.as_view(), name='log_view'),
    path('update/<int:pk>', LogUpdateAPIView.as_view(), name='log_update'),
    path('delete/<int:pk>', LogDestroyAPIView.as_view(), name='log_delete'),
    path('search/', LogSearchListAPIView.as_view(), name='log_search')
]
