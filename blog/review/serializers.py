from rest_framework.serializers import ModelSerializer
from .models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user'] # поля, которые не будут требоваться
    
    def validate(self, attrs):
        super().validate(attrs)
        request = self.context.get("request")
        attrs['user'] = request.user
        return attrs

    # def create(self, validated_data):
    #     request = self.context.get("request")
    #     validated_data['user'] = request.user
    #     return super().create(validated_data)
