from django.contrib import admin
from shows.models import Show, Tag, Rating
# Register your models here.
admin.site.register(Tag)
admin.site.register(Show)
admin.site.register(Rating)
