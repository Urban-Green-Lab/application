from rest_framework import serializers, status
from djangorestapp.models import QuizTaker
from djangorestapp.models import event
from djangorestapp.models import question_bank
from djangorestapp.models import quiz_question
from djangorestapp.models import quiz_bank
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
import string


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
        ##Send email here
        ##Check to see if email isn't null

        if data.get('email', None) :
            email = data.get('email')
            full_name = data.get('fname') + " " + data.get('lname')
            score = data.get('score')
            event_name = event.objects.get(id = data.get('event_id'))
            quiz_name = quiz_bank.objects.get(id = data.get('quiz_bank_id'))
            question_answers = getQuestionAnswers(data.get('quiz_bank_id'))
            send_mail(
                'Thnaks for taking Urban Green Lab Game',
                 get_template('../templates/mail.html').render(
                     Context({
                         'full_name' : full_name,
                         'event_name' : event_name,
                         'quiz_name' : quiz_name,
                         'score' : score,
                         'question_answers' : question_answers
                     })
                 ),
                 'urbangreenlabapp@gmail.com',
                 [email],
                 fail_silently = True
            )        

        return Response(serialized_data.data)
    except Exception as error:
        return Response(
            {"detail": "{e}".format(e=error)}, status=status.HTTP_404_NOT_FOUND
        )


##Construct QuestionAnswer Array for a given quiz id
def getQuestionAnswers(quiz_bank_id):
    ##get an array of the questions
    ## quiz_question = quiz_bank_id, question_bank_id
    ## create an array to hold the question answers
    question_answers = []
    quiz_questions = quiz_question.objects.filter(quiz_bank_id = quiz_bank_id)

    for current_quiz_question in quiz_questions:
        answer = current_quiz_question.answes_set.filter(is_correct = True)
        currentQuestionAnswer = QuestionAnswer(current_quiz_question.question_bank.question, answer, current_quiz_question.question_bank.info_link )
        question_answers.append(currentQuestionAnswer)

    return question_answers
##QuestionAnswer Model
class QuestionAnswer:
    def _init_(self,question, answer, info_link):
        self.question = question
        self.answer = answer
        self.info_link = info_link


class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ["email", "fname", "lname", "event",
                  "quiz_bank", "score", "initials", "zip_code"]
