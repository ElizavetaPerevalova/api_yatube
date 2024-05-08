from api.permissions import isAuthorOrAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Операции CRUD с экземплярами модели пост."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (isAuthorOrAuthenticated, )

    def perform_create(self, serializer):
        """Сохранение объекта."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Операции CRUD с экземплярами модели группа."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Операции CRUD с экземплярами модели комментарий."""
    serializer_class = CommentSerializer
    permission_classes = (isAuthorOrAuthenticated, )

    def get_queryset(self):
        """Возвращает набор объектов."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments

    def perform_create(self, serializer):
        """Сохрание объекта и операции."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)
