from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from .serializers import OrderInputSerializer
from boxes.services.box_selector import BoxSelector


class BoxRecommendationAPIView(APIView):

    @extend_schema(
        request=OrderInputSerializer,
        responses={200: dict}
    )
    def post(self, request):

        serializer = OrderInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = BoxSelector().recommend(
            serializer.validated_data["items"]
        )

        return Response(
            result,
            status=status.HTTP_200_OK
        )