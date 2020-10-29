from . import models
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path
from .forms import (
    QuestionForm,
    QuestionBankAnswerForm,
    QuizBankForm,
    QuizQuestionForm
)
from django.conf.urls import url
from .views import question_post, quiz_post


class MyAdminSite(AdminSite):
    index_template = "tutorial.html"
    index_title = None

    def get_urls(self):
        urls = super().get_urls()

        urls += [
            # Question Paths
            url('questions/create',
                self.admin_view(self.question_view), name="questions"),
            url("question_post/", question_post, name="question_post"),
            url("quizzes/create", self.admin_view(self.quizzes_view), name="quizzes"),
            url("quiz_post/", quiz_post, name="quiz_post"),
        ]
        urls += [
            path('help/', self.admin_view(self.help_view)),
        ]
        return urls

    def help_view(self, request):
        context = dict(
            self.each_context(request),
            app_path=None,
            username=request.user.get_username(),
        )
        return TemplateResponse(request, "tutorial.html", context)

    def question_view(self, request, action=None):
        context = dict(
            self.each_context(request),
            app_path=None,
            username=request.user.get_username(),
            question_form=QuestionForm(),
            answer_form_1=QuestionBankAnswerForm(prefix="a1"),
            answer_form_2=QuestionBankAnswerForm(prefix="a2"),
            answer_form_3=QuestionBankAnswerForm(prefix="a3"),
            answer_form_4=QuestionBankAnswerForm(prefix="a4"),

        )
        return TemplateResponse(request, "question/form.html", context)

    def quizzes_view(self, request, action=None):
        context = dict(
            self.each_context(request),
            app_path=None,
            username=request.user.get_username(),
            quiz_form=QuizBankForm(),
            quiz_question_form_1=QuizQuestionForm(prefix="qq1"),
            quiz_question_form_2=QuizQuestionForm(prefix="qq2"),
            quiz_question_form_3=QuizQuestionForm(prefix="qq3"),
            quiz_question_form_4=QuizQuestionForm(prefix="qq4"),
            quiz_question_form_5=QuizQuestionForm(prefix="qq5"),

        )
        return TemplateResponse(request, "quiz/form.html", context)


admin_site = MyAdminSite(name='myadmin')
# admin_site.index_template = 'sometemplate.html'
# Register your models here.

admin_site.register(models.EventQuiz)
admin_site.register(models.Event)
admin_site.register(models.QuestionBankAnswer)
admin_site.register(models.QuestionBank)
admin_site.register(models.QuizBank)
admin_site.register(models.QuizQuestion)
admin_site.register(models.QuizTaker)
