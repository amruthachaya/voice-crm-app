from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TranscriptSerializer
from .services.extractor import extract_entities


class ExtractDataAPIView(APIView):
    def post(self, request):
        serializer = TranscriptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transcript = serializer.validated_data["transcript"]

        extracted_data = extract_entities(transcript)

        return Response(extracted_data, status=status.HTTP_200_OK)
