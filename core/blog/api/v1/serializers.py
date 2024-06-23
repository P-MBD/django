from rest_framework import serializers
from ...models import Post,Category

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_path = serializers.URLField(source="get_absolute_api_url", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "content",
            "snippet",
            "category",
            "status",
            "relative_path",
            "created_date",
            "published_date",
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


