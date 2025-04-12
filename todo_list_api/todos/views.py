
from rest_framework.exceptions import PermissionDenied
from drf_yasg.utils import swagger_auto_schema  # for swagger docs
from drf_yasg import openapi
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics, permissions  

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]  # only for logged-in users

    @swagger_auto_schema(  # doc for GET todos
        operation_description="Get the list of todos for the authenticated user",
        responses={200: TodoSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(  # doc for creating a todo
        operation_description="Create a new todo item",
        request_body=TodoSerializer,
        responses={201: TodoSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)  # only return current user's todos

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # assign todo to current user


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(  # doc for retrieving one todo
        operation_description="Retrieve a specific todo item",
        responses={200: TodoSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(  # doc for updating a todo
        operation_description="Update a specific todo item",
        request_body=TodoSerializer,
        responses={200: TodoSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(  # doc for deleting a todo
        operation_description="Delete a specific todo item",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)  # limit access to own todos

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:  # block editing others' todos
            raise PermissionDenied("Forbidden")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:  # block deleting others' todos
            raise PermissionDenied("Forbidden")
        instance.delete()

