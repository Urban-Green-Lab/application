from django.http import HttpResponse
from .. import models
from django.shortcuts import get_object_or_404, redirect


def question_post(request):
    if request.method == "POST":
        data = request.POST
        question_info = {
            "question": data.get("question", None),
            "image": data.get("image", None),
            "value": int(data.get("value", None)),
            "info_link": data.get("info_link", None)
        }

        question_bank = models.QuestionBank.objects.create(
            question=question_info["question"],
            image=question_info["image"],
            value=question_info["value"],
            info_link=question_info["info_link"],
        )

        answers_info = [
            {
                "answer": data.get("a1-answer", None),
                "is_correct": True if data.get("a1-is_correct", None) else False,
            },
            {
                "answer": data.get("a2-answer", None),
                "is_correct": True if data.get("a2-is_correct", None) else False
            },
            {
                "answer": data.get("a3-answer", None),
                "is_correct": True if data.get("a3-is_correct", None) else False
            },
            {
                "answer": data.get("a4-answer", None),
                "is_correct": True if data.get("a4-is_correct", None) else False
            }
        ]

        for answer in answers_info:
            if answer["answer"]:
                models.QuestionBankAnswer.objects.create(
                    answer=answer["answer"],
                    is_correct=answer["is_correct"],
                    question_bank=question_bank
                )

        return redirect('admin:question_detail', question_id=question_bank.id)


def question_detail(request, question_id=None):
    if question_id:
        question = get_object_or_404(models.QuestionBank, pk=question_id)
        print(question)
        return HttpResponse(f"Question {question_id}")
