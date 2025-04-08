from django.contrib import admin
from .models import Request, RequestHistory, Review


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'owner',
        'executor',
        'type',
        'priority',
        'location',
        'status',
        'created_at',
    )
    list_filter = ('status', 'type', 'priority', 'location')
    search_fields = ('name', 'description',
                     'owner__username', 'executor__username')


@admin.register(RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ('request', 'status', 'date')
    list_filter = ('status',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('request', 'executor', 'rating')
    list_filter = ('rating',)
