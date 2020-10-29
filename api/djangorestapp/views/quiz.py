from django.http import HttpResponse
from ..models import QuizBank, QuizQuestion, QuestionBank
from django.shortcuts import get_object_or_404


def quiz_post(request):
    if request.method == "POST":
        data = request.POST
        quiz_bank = QuizBank.objects.create(
            name=data.get("name"),
            timer=int(data.get("timer"))
        )

        for key, value in data.items():
            if "question_bank" in key and value:
                question = get_object_or_404(QuestionBank, pk=int(value))
                QuizQuestion.objects.create(
                    quiz_bank=quiz_bank,
                    question_bank=question
                )

        return HttpResponse("Quiz created add quiz details view here")
