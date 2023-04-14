from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance:Post):
        rep = super().to_representation(instance)
        # rep['likes'] = Like.objects.filter(post=instance).count()
        rep['likes'] = instance.likes.all().count()
        return rep
