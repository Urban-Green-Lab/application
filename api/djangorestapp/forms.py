from django import forms
from .models import (QuestionBank, QuestionBankAnswer,
                     QuizBank, QuizQuestion, Event, EventQuiz)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionBank
        fields = ["question", "image", "value", "info_link"]


class QuestionBankAnswerForm(forms.ModelForm):

    answer = forms.CharField(required=False)

    class Meta:
        model = QuestionBankAnswer
        fields = ("answer", "is_correct")


class QuizBankForm(forms.ModelForm):
    class Meta:
        model = QuizBank
        fields = ["name", "timer", ]


class QuizQuestionForm(forms.ModelForm):
    question_bank = forms.ModelChoiceField(queryset=QuestionBank.objects.all(), label="Question")

    class Meta:
        model = QuizQuestion
        fields = ["question_bank"]


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ["name", "active", "child_mode", ]


class EventQuizForm(forms.ModelForm):
    class Meta:
        model = EventQuiz
        fields = ["quiz"]
