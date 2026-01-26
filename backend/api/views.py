from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .evaluator.evals import evaluate_extraction, generate_excel_report
from .extractor import extract_entities
from .serializers import TranscriptSerializer


class ExtractDataAPIView(APIView):
    def post(self, request):
        try:
            serializer = TranscriptSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            transcript = serializer.validated_data["transcript"]
            extracted_data = extract_entities(transcript)
            return Response(extracted_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class EvaluationAPIView(APIView):
    def get(self, request):
        try:
            df = evaluate_extraction()
            df =df.fillna("")
            return Response(df.to_dict(orient="records"), status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EvaluationExcelAPIView(APIView):
    def get(self, request):
        try:
            file_path = generate_excel_report()
            return Response(
                    {"message": "Excel generated", "file": file_path},
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

