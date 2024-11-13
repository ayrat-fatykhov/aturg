from rest_framework import generics

from logs.models import Log
from logs.serializers import LogSerializer


class LogCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание Лога
    """
    serializer_class = LogSerializer


class LogListAPIView(generics.ListAPIView):
    """
    Отвечает за отображение списка Логов
    """
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class LogRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за отображение Лога
    """
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class LogUpdateAPIView(generics.UpdateAPIView):
    """
    Отвечает за изменение Лога
    """
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class LogDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление Лога
    """
    queryset = Log.objects.all()


class LogSearchListAPIView(generics.ListAPIView):
    """
    Отвечает за фильтрацию Логов
    """
    serializer_class = LogSerializer

    def get_queryset(self):
        qs = self.request.data
        if qs != {}:
            if 'name' in qs and 'date' in qs:
                return Log.objects.filter(name__contains=qs['name'], date__contains=qs['date'])
            elif 'name' in qs:
                return Log.objects.filter(name__contains=qs['name'])
            elif 'date' in qs:
                return Log.objects.filter(date__contains=qs['date'])
