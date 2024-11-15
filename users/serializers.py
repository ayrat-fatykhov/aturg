from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Пользователя
    """
    class Meta:
        model = User
        fields = '__all__'
