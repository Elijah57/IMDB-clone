from watchlist_app.models import Review, Media, StreamPlatform
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from watchlist_app.api.serializers import MediaSerializer, ReviewSerializer, StreamSeriaizer
from watchlist_app.api.permissions import IsAdminOrReadOnly,IsReviewUserOrReadOnly
from rest_framework.exceptions import ValidationError


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        pk = self.kwargs["pk"]
        media_instance = Media.objects.get(id=pk)
        
        #avoid a user reviewing twice
        if Review.objects.filter(the_user=user, media=media_instance).exists():
            raise ValidationError("You have given a review already!!")
        
        if media_instance.num_rating == 0:
            media_instance.avg_rating = serializer.validated_data["rating"]

        else:
            media_instance.avg_rating = (media_instance.avg_rating + serializer.validated_data["rating"])/ 2
        
        media_instance.num_rating = media_instance.num_rating + 1
        media_instance.save()
        serializer.save(the_user=user,media=media_instance)


class MediaReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = []

    def get_queryset(self):
        pk = self.kwargs["pk"]
        media_instance = Media.objects.get(id=pk)
        return Review.objects.filter(media=media_instance)

class MediaReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly] 
    
    def get_object(self):
        user = self.request.user
        pk = self.kwargs["pk"]
        media_instance = Media.objects.get(id=pk)
        return Review.objects.get(the_user=user, media=media_instance)


class MediaList(APIView):
    permission_classes = [IsAdminOrReadOnly,]
    def get(self, request):
        media_instances = Media.objects.all()
        serializer = MediaSerializer(media_instances, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MediaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, PATCH and DELETE to serve a media instance detail"""
    permission_classes = [IsAdminOrReadOnly]
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    lookup_field = "pk"

    
class StreamList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSeriaizer

class StreamDetail(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, PATCH and DELETE to serve a stream instance detail"""
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSeriaizer
    lookup_field = "pk"