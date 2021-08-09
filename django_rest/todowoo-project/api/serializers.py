from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # to make a field we need serializers.ReadOnlyField() so other people can see but can't edit
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo  # we need a model to work with serializer so we imported Todo model form todo app
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']


class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo  # we need a model to work with serializer so we imported Todo model form todo app
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'datecompleted', 'important']
