from watchlist_app.models import Review, Media, StreamPlatform
from rest_framework import serializers 


class StreamSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"

class MediaSerializer(serializers.HyperlinkedModelSerializer):

    platform = serializers.HyperlinkedIdentityField(view_name="stream_detail", )
    review_set = serializers.StringRelatedField(many=True, )
    class Meta:
        model = Media
        fields = "__all__"
        
        extra_kwargs = {
            "url": {"view_name": "media_detail", "lookup_field": "pk"}
        }

class ReviewSerializer(serializers.ModelSerializer):
    the_user = serializers.StringRelatedField()
    class Meta:
        model = Review
        # fields = ["the_user", "rating", "comment", "active"]
        exclude = ["media", ]
        lookup_field = "pk"