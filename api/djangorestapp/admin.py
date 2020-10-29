from . import models
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path
from .forms import (
    QuestionForm,
    QuestionBankAnswerForm,
    QuizBankForm,
    QuizQuestionForm,
    EventForm, EventQuizForm,
)
from django.conf.urls import url
from .views import question_post, quiz_post, event_post, quiz_detail, event_detail
import datetime
from django.shortcuts import get_object_or_404


class MyAdminSite(AdminSite):
    index_template = "tutorial.html"
    index_title = None

    def get_urls(self):
        urls = super().get_urls()

        urls += [
            # Question Paths
            url('questions/create',
                self.admin_view(self.question_view), name="questions"),
            url(r"questions/detail/(?P<question_id>\d+)/",
                self.admin_view(self.question_view), name="question_detail"),
            url("question_post/", question_post, name="question_post"),

            url("quizzes/create", self.admin_view(self.quizzes_view), name="quizzes"),
            url(r"quizzes/detail/(?P<quiz_id>\d+)/",
                quiz_detail, name="quiz_detail"),
            url("quiz_post/", quiz_post, name="quiz_post"),

            url("events/create", self.admin_view(self.events_view), name="events"),
            url(r"events/detail/(?P<event_id>\d+)/",
                event_detail, name="event_detail"),
            url("event_post/", event_post, name="event_post"),
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

    def question_view(self, request, question_id=None):
        action = request.get_full_path().split('/')[3]
        if action == "create":
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
        if action == "detail":
            question = get_object_or_404(models.QuestionBank, pk=question_id)
            answers = models.QuestionBankAnswer.objects.filter(
                question_bank=question)

            print(answers)
            context = dict(
                self.each_context(request),
                app_path=None,
                username=request.user.get_username(),
                question=question,
                answers=answers
            )
            return TemplateResponse(request, "question/detail.html", context)
        if action == "list":
            pass
        if action == "edit":
            pass

    def quizzes_view(self, request, action=None):
        action = request.get_full_path().split('/')[3]
        if action == "create":
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
        if action == "detail":
            pass
        if action == "list":
            pass
        if action == "edit":
            pass

    def events_view(self, request, action=None):
        action = request.get_full_path().split('/')[3]
        if action == "create":
            context = dict(
                self.each_context(request),
                app_path=None,
                username=request.user.get_username(),
                event_form=EventForm(),
                event_quiz_form=EventQuizForm(),
                date=datetime.date.strftime(datetime.date.today(), "%m/%d/%Y")
            )
            return TemplateResponse(request, "event/form.html", context)
        if action == "detail":
            pass
        if action == "list":
            pass
        if action == "edit":
            pass


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
