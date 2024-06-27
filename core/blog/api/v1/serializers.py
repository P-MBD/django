from rest_framework import serializers
from ...models import Post,Category
from accounts.models import Profile, User
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_path = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Post
        fields = ["id","author","image","title", "content","snippet","category","status","absolute_url","relative_path","created_date","published_date"]
        read_only_fields = ['author']
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        #rep['state']= 'list'
        if request.parser_context.get('kwargs').get('pk'):
            #rep['state'] = 'single'
            rep.pop('snippet', None)
            rep.pop('relative_path', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content',None)
        rep['category'] = CategorySerializer(instance.category, context = {'request': request}).data
        rep.pop('snippet', None)
        return rep
    def create(self, validated_data):
        user = User.objects.get(id = self.context.get('request').user.id)
        validated_data['author'] = Profile.objects.get(user = user )
        return super().create(validated_data)



