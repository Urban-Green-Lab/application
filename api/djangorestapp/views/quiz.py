from django.http import HttpResponse
from ..models import QuizBank, QuizQuestion, QuestionBank
from django.shortcuts import get_object_or_404, redirect
import json


def quiz_post(request):
    if request.method == "POST":
        data = request.POST
        quiz_id = data.get("quiz_id", None)
        if quiz_id:
            quiz = get_object_or_404(QuizBank, pk=int(quiz_id))

            quiz.name = data.get("name")
            quiz.timer = int(data.get("timer"))
            quiz.save()
            quiz_question_ids = json.loads(data.get("quiz_question_ids"))

            for key, value in data.items():
                if "question_bank" in key:
                    index = int(key.split("-")[0][2:]) - 1
                    quiz_question_id = (quiz_question_ids[index])
                    if quiz_question_id:
                        quiz_question = get_object_or_404(QuizQuestion, pk=quiz_question_id)
                        if value:
                            question = get_object_or_404(QuestionBank, pk=int(value))
                            quiz_question.question_bank = question
                            quiz_question.save()
                        else:
                            quiz_question.delete()
                    else:
                        # create
                        if value:
                            question = get_object_or_404(QuestionBank, pk=int(value))
                            QuizQuestion.objects.create(
                                quiz_bank=quiz,
                                question_bank=question
                            )
                    

            return redirect('admin:quiz_detail', quiz_id=quiz.id)
        else:
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
