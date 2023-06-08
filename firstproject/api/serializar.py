from rest_framework import serializers
class StudentSerializers(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 90)