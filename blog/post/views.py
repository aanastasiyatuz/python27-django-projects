from django.shortcuts import render
from .models import Post


def posts_list(request):
    queryset = Post.objects.all()
    return render(request, 'listing.html', {'posts':queryset})



"REST"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def posts_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_details(request, id):
    # Post.objects.filter(id=id).first()
    # Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=204)
