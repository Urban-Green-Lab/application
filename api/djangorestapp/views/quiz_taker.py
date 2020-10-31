from rest_framework import serializers, status
from djangorestapp.models import (
    QuizTaker, Event, QuestionBank, QuizQuestion, QuizBank)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
import string
from django.template.response import TemplateResponse
from django.contrib.staticfiles import finders
from django.core.mail import EmailMultiAlternatives



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
        # Send email here
        # Check to see if email isn't null

        if data.get('email', None):
            quiz_bank_id = data.get('quiz_bank')
            email = data.get('email')
            full_name = data.get('fname') + " " + data.get('lname')
            score = data.get('score')
            event_name = Event.objects.get(id=data.get('event')).name
            quiz_name = QuizBank.objects.get(id=quiz_bank_id).name

            question_answers = getQuestionAnswers(quiz_bank_id)



            plaintext = get_template("mail.html")
            htmly     = get_template("mail.html")

            context = {
                        'full_name': full_name,
                        'event_name': event_name,
                        'quiz_name': quiz_name,
                        'score': score,
                        'question_answers': question_answers
            }

            subject, from_email, to = (
                'Thank you for registering to our site', 
                'urbangreenlabapp@example.com', 
                email
            )

            text_content = plaintext.render(context)
            html_content = htmly.render(context)
            msg = EmailMultiAlternatives(subject, "html_content", from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


        return TemplateResponse(request, "mail.html", {
            'full_name': full_name,
            'event_name': event_name,
            'quiz_name': quiz_name,
            'score': score,
            'question_answers': question_answers
        })
        # return Response(serialized_data.data)
    except Exception as error:
        return Response(
            {"detail": "{e}".format(e=error)}, status=status.HTTP_404_NOT_FOUND
        )


# Construct QuestionAnswer Array for a given quiz id
def getQuestionAnswers(quiz_bank_id):
    # get an array of the questions
    ## quiz_question = quiz_bank_id, question_bank_id
    # create an array to hold the question answers
    question_answers = []
    quiz_questions = QuizQuestion.objects.filter(quiz_bank_id=quiz_bank_id)

    for current_quiz_question in quiz_questions:
        answer = current_quiz_question.question_bank.questionbankanswer_set.filter(
            is_correct=True)
        currentQuestionAnswer = QuestionAnswer(
            current_quiz_question.question_bank.question, answer, current_quiz_question.question_bank.info_link)
        question_answers.append(currentQuestionAnswer)

    return question_answers
# QuestionAnswer Model


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
