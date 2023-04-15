import django_filters

from .models import Record

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = '__all__'
        # Don't show
        exclude = ['brief_description', 'username', 'video_link']
