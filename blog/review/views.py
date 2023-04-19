from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post.models import Post, User
from .models import Comment, Like
from .serializers import CommentSerializer


@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():
        # если лайк есть, то удаляем его
        Like.objects.filter(user=user, post=post).delete()
    else:
        # если нет, создаем
        Like.objects.create(user=user, post=post)
    return Response(status=201)


class CreateCommentAPIView(CreateAPIView):
    """
    Создание комментария
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
