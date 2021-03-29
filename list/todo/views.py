from todo.permissions import IsOwnerOrReadOnly
from rest_framework.generics import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import PostSerializer
from .models import Todo

# Create your views here.

