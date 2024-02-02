from django.contrib import admin
from watchlist_app.models import Review, Media, StreamPlatform

# Register your models here.
admin.site.register(Review)
admin.site.register(Media)
admin.site.register(StreamPlatform)