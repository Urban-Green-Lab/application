from rest_framework import serializers, status
from djangorestapp.models import QuizTaker
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('POST',))
def post_quiz_taker(request):
    try:
        data = request.data
        serialized_data = QuizTakerSerializer(data=data)
        is_valid = serialized_data.is_valid()
        if not is_valid:
            return Response(
                {"detail": serialized_data.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serialized_data.save()
        return Response(serialized_data.data)
    except Exception as error:
        return Response(
            {"detail": "{e}".format(e=error)}, status=status.HTTP_404_NOT_FOUND
        )


class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ["email", "fname", "lname", "event",
                  "quiz_bank", "score", "initials", "zip_code"]
