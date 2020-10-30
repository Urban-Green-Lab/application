from django.db import models
from .event import Event
from .quiz_bank import QuizBank


class QuizTaker(models.Model):
    """Quiz Taker Model

    Description: stores the informatin for a single quiz taker

    Fields
    - email = `EmailField(max_length=255)`
    - fname = `CharField(max_length=255, blank=True, null=True)`
    - lname = `CharField(max_length=255, blank=True, null=True)`
    - event = `ForeignKey(Event, on_delete=models.DO_NOTHING)`
    - quiz_bank = `ForeignKey(QuizBank, on_delete=models.DO_NOTHING)`
    - score = `IntegerField()`
    - initials = `CharField(max_length=3)`
    """
    email = models.EmailField(max_length=255, blank=True, null=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quiz_bank = models.ForeignKey(QuizBank, on_delete=models.CASCADE)
    score = models.IntegerField()
    initials = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        ordering = ["lname"]
        verbose_name_plural = "quiz takers"

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email
