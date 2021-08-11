from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES




                    # # # # # # # # # # # # # #
                    #   HYPERLINK SERIALIZER  #
                    # # # # # # # # # # # # # #

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')


from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)







                    # # # # # # # # # # #
                    #   PK SERIALIZER   #
                    # # # # # # # # # # #


#
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#
# from django.contrib.auth.models import User
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())







                    # # # # # # # # # # #
                    # BASIC SERIALIZER  #
                    # # # # # # # # # # #


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_date):
#         return Snippet.objects.create(**validated_date)
#
#     def update(self, instance, validated_date):
#         instance.title = validated_date.get('title', instance.title)
#         instance.code = validated_date.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
