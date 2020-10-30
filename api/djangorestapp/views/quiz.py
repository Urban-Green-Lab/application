from django.http import HttpResponse
from ..models import QuizBank, QuizQuestion, QuestionBank
from django.shortcuts import get_object_or_404, redirect


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

        return redirect('admin:quiz_detail', quiz_id=quiz_bank.id)


def quiz_detail(request, quiz_id=None):
    if quiz_id:
        quiz = get_object_or_404(QuizBank, pk=quiz_id)
        return HttpResponse(f"Quiz {quiz_id}")
