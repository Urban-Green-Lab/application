from django.db import models
from .question_bank import QuestionBank


class QuestionBankAnswer(models.Model):
    """Question Bank Answer Model

    Description: Stores a single answer to a question in the question bank


    Fields
    - answer = `CharField(max_length=255)`
    - is_correct = `BooleanField(default=False)`
    - question_bank = `ForeignKey(QuestionBank, related_name="questions", on_delete=CASCADE)`
    """
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question_bank = models.ForeignKey(
        QuestionBank, on_delete=models.CASCADE)

    class Meta:
        ordering = ["?"]
        verbose_name_plural = "question bank answers"

    def __str__(self):
        return self.answer

    def __unicode__(self):
        return self.answer
