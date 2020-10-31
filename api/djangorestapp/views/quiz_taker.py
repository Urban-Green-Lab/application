from rest_framework import serializers, status
from djangorestapp.models import (
    QuizTaker, Event, QuizQuestion, QuizBank)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.template.loader import get_template
from threading import Thread
from djangorestproj import settings

EMAIL_HEADER_URL = "https://firebasestorage.googleapis.com/v0/b/urban-green-lab-quiz.appspot.com/o/Screen%20Shot%202020-10-30%20at%209.42.37%20PM.png?alt=media&token=4ab97143-d858-4ddf-a29e-bc65b4b4447d"


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

        if data.get('email', None):
            Thread(target=send_email, args=(data, )).start()

        return Response(serialized_data.data)
    except Exception as error:
        return Response(
            {"detail": "{e}".format(e=error)}, status=status.HTTP_404_NOT_FOUND
        )


def getQuestionAnswers(quiz_bank_id):
    question_answers = []
    quiz_questions = QuizQuestion.objects.filter(quiz_bank_id=quiz_bank_id)

    for question in quiz_questions:
        answer = question.question_bank.questionbankanswer_set.get(
            is_correct=True
        )
        currentQuestionAnswer = QuestionAnswer(
            question.question_bank.question,
            answer,
            question.question_bank.info_link
        )
        question_answers.append(currentQuestionAnswer)

    return question_answers


class QuestionAnswer():
    def __init__(self, question, answer, info_link):
        self.question = question
        self.answer = answer
        self.info_link = info_link


class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ["email", "fname", "lname", "event",
                  "quiz_bank", "score", "initials", "zip_code"]


def send_email(data):
    quiz_bank_id = data.get('quiz_bank')
    email = data.get('email')
    full_name = data.get('fname') + " " + data.get('lname')
    score = data.get('score')
    event_name = Event.objects.get(id=data.get('event')).name
    quiz_name = QuizBank.objects.get(id=quiz_bank_id).name

    question_answers = getQuestionAnswers(quiz_bank_id)

    plaintext = get_template("mail.txt")
    htmly = get_template("mail.html")

    context = {
        'full_name': full_name,
        'event_name': event_name,
        'quiz_name': quiz_name,
        'score': score,
        'question_answers': question_answers,
    }

    subject, from_email, to = (
        settings.SUBJECT_TEXT,
        settings.DEFAULT_FROM_EMAIL,
        email
    )

    text_content = plaintext.render(context)
    html_content = htmly.render(context)

    send_mail(subject, text_content, from_email, [
        to], fail_silently=True,
        html_message=html_content
    )
