from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class QuizBank(SafeDeleteModel):
    """Quiz Bank Model

    Description: Stores a single quiz for the quiz bank

    If a Quiz is deleted it is just masked so that it can still be accessed from the QuizTaker Model.

    Fields
    - name = `CharField(max_length=255)`
    - timer = `IntegerField` in minutes
    """
    # Added this because the important quiz_taker model uses
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=255)
    timer = models.IntegerField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "quiz banks"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
