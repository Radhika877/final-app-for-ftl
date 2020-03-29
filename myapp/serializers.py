from rest_framework_json_api import serializers
from myapp.models import user, activity_periods

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class activity_periodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = activity_periods
        fields = '__all__'
