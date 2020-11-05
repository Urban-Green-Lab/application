from rest_framework import serializers, status
from djangorestapp.models import QuizTaker, Event
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


@api_view(('GET',))
def get_leaderboard(request):
    try:
        active_event = get_object_or_404(Event, active=True)
        quiz_taker = QuizTaker.objects.filter(
            event=active_event).order_by('-score')
        serializer = QuizTakerSerializer(quiz_taker, many=True)
        return Response(serializer.data)
    except Exception as error:
        return Response(
            {"detail": "{e}".format(e=error)},
            status=status.HTTP_404_NOT_FOUND
        )


class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ["score", "initials"]
