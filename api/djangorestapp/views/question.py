from .. import models
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404


def question_form(request):
    if request.method == "POST":
        data = request.POST
        is_update = data.get("question_id", False)
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

        question_info = {
            "id": data.get("question_id", None),
            "question": data.get("question", None),
            "info_link": data.get("info_link", None),
            "info_text": data.get("info_text", None)
        }

        if is_update:
            question_bank = get_object_or_404(
                models.QuestionBank, pk=question_info["id"])

            question_bank.question = question_info["question"]
            question_bank.info_link = question_info["info_link"]
            question_bank.info_text = question_info["info_text"]
            question_bank.save()
            answer_ids = json.loads(data.get("answers"))
            for i in range(len(answers_info)):
                form_answer = answers_info[i]
                if answer_ids[i]:
                    answer = get_object_or_404(
                        models.QuestionBankAnswer, pk=answer_ids[i]["id"])
                    if form_answer["answer"].strip():
                        answer.answer = form_answer["answer"]
                        answer.is_correct = form_answer["is_correct"]
                        answer.save()
                    else:
                        answer.delete()
                else:
                    if form_answer["answer"]:
                        models.QuestionBankAnswer.objects.create(
                            answer=form_answer["answer"],
                            is_correct=form_answer["is_correct"],
                            question_bank=question_bank
                        )

            return redirect('admin:question_detail', question_id=question_bank.id)
        else:

            question_bank = models.QuestionBank.objects.create(
                question=question_info["question"],
                info_link=question_info["info_link"],
                info_text=question_info["info_text"],
            )

            for answer in answers_info:
                if answer["answer"]:
                    models.QuestionBankAnswer.objects.create(
                        answer=answer["answer"],
                        is_correct=answer["is_correct"],
                        question_bank=question_bank
                    )

            return redirect('admin:question_detail', question_id=question_bank.id)
