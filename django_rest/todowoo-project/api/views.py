from django.utils import timezone
from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoCompleteSerializer
from todo.models import Todo


# show completed todos
class TodoCompleted(generics.ListAPIView):  # ListAPIView is to show a list from the database
    serializer_class = TodoSerializer

    # to view the data someone must be lodged in before view the data
    permission_classes = [permissions.IsAuthenticated]

    # only view the data that relevant to them
    def get_queryset(self):
        user = self.request.user  # to get the current user who is lodged in
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')


class TodoListCrete(generics.ListCreateAPIView):  # ListCreateAPIView is to show a list from the database and create
    serializer_class = TodoSerializer

    # to view the data someone must be lodged in before view the data
    permission_classes = [permissions.IsAuthenticated]

    # only view the data that relevant to them
    def get_queryset(self):
        user = self.request.user  # to get the current user who is lodged in
        return Todo.objects.filter(user=user, datecompleted__isnull=True)

    # to create a todo we need this function
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView):  # RetrieveUpdateDestroyAPIView is to show, delete, and update
    serializer_class = TodoSerializer

    # to view the data someone must be lodged in before view the data
    permission_classes = [permissions.IsAuthenticated]

    # only view the data that relevant to them
    def get_queryset(self):
        user = self.request.user  # to get the current user who is lodged in
        return Todo.objects.filter(user=user)


class TodoComplete(generics.UpdateAPIView):  # UpdateAPIView is to update
    serializer_class = TodoCompleteSerializer

    # to view the data someone must be lodged in before view the data
    permission_classes = [permissions.IsAuthenticated]

    # only view the data that relevant to them
    def get_queryset(self):
        user = self.request.user  # to get the current user who is lodged in
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()