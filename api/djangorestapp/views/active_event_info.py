from rest_framework import serializers, status
from djangorestapp.models import (
    Event,
    EventQuiz,
    QuizQuestion,
    QuestionBankAnswer
)
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET',))
def get_active_event_info(request):
    try:
        active_event = get_object_or_404(Event, active=True)
        seralized_data = ActiveEventSerializer(active_event)
        return Response(seralized_data.data)
    except Exception as error:
        return Response(
            {"detail": "{e}".format(e=error)},
            status=status.HTTP_404_NOT_FOUND
        )


class ActiveEventSerializer(serializers.Serializer):
    event_id = serializers.SerializerMethodField()
    child_mode = serializers.BooleanField()
    quiz_id = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    def get_event_id(self, obj):
        id = obj.id
        return id

    def get_quiz_id(self, obj):
        return self.get_quiz(obj).id

    def get_questions(self, obj):
        quiz = self.get_quiz(obj)
        event_quiz = get_list_or_404(QuizQuestion, quiz_bank_id=quiz.id)
        question_bank = QuizQuestionSerializer(event_quiz, many=True).data
        questions = []
        for question in question_bank:
            current_q = dict(question["question_bank"])
            id = current_q["id"]
            current_q["question_id"] = id
            current_q["answers"] = QuestionBankAnswerSerializer(
                get_list_or_404(
                    QuestionBankAnswer, question_bank_id=id
                ), many=True
            ).data
            del current_q["id"]
            questions.append(current_q)
        return questions

    def get_quiz(self, event):
        event_quiz = get_object_or_404(EventQuiz, event_id=event.id)
        return event_quiz.quiz


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ["question_bank"]
        depth = 1


class QuestionBankAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBankAnswer
        fields = ["answer", "is_correct"]
