from django import forms
from .models import QuestionBank, QuestionBankAnswer


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
