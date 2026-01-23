from rest_framework import serializers

class TranscriptSerializer(serializers.Serializer):
    transcript = serializers.CharField()
