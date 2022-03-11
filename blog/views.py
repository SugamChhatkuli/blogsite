from django.shortcuts import render
from .serializers import BlogSerializer, ProfileSerializer, BlogLikeSerializer
from .models import Blog, Profile
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class= BlogSerializer
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        data = request.data
        serial = self.serializer_class(data = data)
        if serial.is_valid():
            user = Profile.objects.get(user = request.user)
            serial.save(author = user)
            return Response(serial.data,status = status.HTTP_201_CREATED)
        return  Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)

class BlogLikeView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class= BlogLikeSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field ='pk'

    def post(self,request, *args, **kwargs):
        user = request.user
        blog_id = kwargs['pk']
        blog_obj = Blog.objects.get(id=blog_id)
        profile =Profile.objects.get(user=user)
        print(profile)
        if profile in blog_obj.liked.all():
            print({'msg':'here'})
            blog_obj.liked.remove(profile)
        else:
            blog_obj.liked.add(profile)
            

        # like,created = Like.objects.get_or_create(user=profile, blog_id=blog_id)

        # if not created:
        #     if like.value == 'like':
        #         like.value = 'Unlike'
        #     else:
        #         like.value = 'like'
        # else:
        #     like.value = 'like'

        blog_obj.save()
        return Response()
        

class UpdateProfileView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,]

class UpdateBlogView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes =[IsAuthenticated,]
