from rest_framework import serializers
from .models import Blog, Profile

class BlogSerializer(serializers.ModelSerializer):
    totallike = serializers.SerializerMethodField()

    def get_totallike(self, obj):
        return obj.no_likes()
    class Meta:
        model = Blog
        fields=['id','title','desc','banner_img','liked','author','totallike']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profile
        fields=['id','user','address','contract','profile_img','bio']

class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields=['liked']

