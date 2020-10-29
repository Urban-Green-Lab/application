from django import forms
from .models import QuestionBank, QuestionBankAnswer, QuizBank, QuizQuestion


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionBank
        fields = ["question", "image", "value", "info_link"]


class QuestionBankAnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(QuestionBankAnswerForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['answer'].required = False

    class Meta:
        model = QuestionBankAnswer
        fields = ("answer", "is_correct")


class QuizBankForm(forms.ModelForm):
    class Meta:
        model = QuizBank
        fields = ["name", "timer", ]


class QuizQuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(QuizQuestionForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['question_bank'].required = False

    class Meta:
        model = QuizQuestion
        fields = ["question_bank"]
