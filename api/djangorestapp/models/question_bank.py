from django.db import models


class QuestionBank(models.Model):
    """Question Bank Model

    Description: Stores a single question for the question bank

    Fields
    - question = `CharField(max_length=255)`
    - info_link = `URLField(max_length=200, blank=True, null=True)`
    """
    question = models.CharField(max_length=255)
    info_link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["question"]
        verbose_name_plural = "Question Banks"

    def __str__(self):
        return self.question

    def __unicode__(self):
        return self.question
