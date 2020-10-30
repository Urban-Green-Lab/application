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
from .views import question_form, quiz_post, event_post, quiz_detail, event_detail
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json


class MyAdminSite(AdminSite):
    index_template = "tutorial.html"
    index_title = None

    def get_urls(self):
        urls = super().get_urls()
        question_urls = [
            url('questions/create',
                self.admin_view(self.question_view), name="questions_create"),
            url('questions/list',
                self.admin_view(self.question_view), name="questions_list"),
            url(r"questions/detail/(?P<question_id>\d+)/",
                self.admin_view(self.question_view), name="question_detail"),
            url(r"questions/edit/(?P<question_id>\d+)/",
                self.admin_view(self.question_view), name="question_edit"),
            url("question_form/", question_form, name="question_form"),
        ]

        quiz_urls = [
            url("quizzes/create", self.admin_view(self.quizzes_view), name="quizzes"),
            url(r"quizzes/detail/(?P<quiz_id>\d+)/",
                self.admin_view(self.quizzes_view), name="quiz_detail"),
            url("quiz_post/", quiz_post, name="quiz_post"),
        ]

        event_urls = [
            url("events/create", self.admin_view(self.events_view), name="events"),
            url(r"events/detail/(?P<event_id>\d+)/",
                self.admin_view(self.events_view), name="event_detail"),
            url("event_post/", event_post, name="event_post"),
        ]

        other_urls = [
            path('help/', self.admin_view(self.help_view)),
        ]
        urls += (
            event_urls
            + quiz_urls
            + question_urls
            + other_urls
        )

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
        print(action)
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
            questions = models.QuestionBank.objects.all()
            context = dict(
                self.each_context(request),
                app_path=None,
                username=request.user.get_username(),
                questions=questions,
            )
            return TemplateResponse(request, "question/list.html", context)
        if action == "edit":
            question = get_object_or_404(
                models.QuestionBank.objects.filter(pk=question_id))
            answer_inst = question.questionbankanswer_set.all()
            answers = [None, None, None, None]
            for i in range(len(answers)):
                if answer_inst.count() > i:
                    answers[i] = answer_inst[i]

            def get_answer(index):
                answer = None
                if answers[index]:
                    answer = answers[index].__dict__
                    del answer["_state"]
                    print(answer)
                return answer
            answers = [
                get_answer(0),
                get_answer(1),
                get_answer(2),
                get_answer(3)
            ]
            context = dict(
                self.each_context(request),
                app_path=None,
                username=request.user.get_username(),
                question=question,
                question_form=QuestionForm(initial=question.__dict__),
                answer_form_1=QuestionBankAnswerForm(
                    prefix="a1", initial=answers[0]),
                answer_form_2=QuestionBankAnswerForm(
                    prefix="a2", initial=answers[1]),
                answer_form_3=QuestionBankAnswerForm(
                    prefix="a3", initial=answers[2]),
                answer_form_4=QuestionBankAnswerForm(
                    prefix="a4", initial=answers[3]),
                answers=json.dumps(answers)

            )
            return TemplateResponse(request, "question/form.html", context)

    def quizzes_view(self, request, quiz_id=None):
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
            quiz = get_object_or_404(models.QuizBank, pk=quiz_id)
            questions = [quizquestion.question_bank for quizquestion in models.QuizQuestion.objects.filter(
                quiz_bank=quiz)]

            print(questions)
            context = dict(
                self.each_context(request),
                app_path=None,
                username=request.user.get_username(),
                quiz=quiz,
                questions=questions,
            )
            return TemplateResponse(request, "quiz/detail.html", context)
        if action == "list":
            pass
        if action == "edit":
            pass

    def events_view(self, request, event_id=None):
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
            event = get_object_or_404(models.Event, pk=event_id)
            quizzes = [event_quiz.quiz for event_quiz in models.EventQuiz.objects.filter(
                event=event)]
            context = dict(
                self.each_context(request),
                app_path=None,
                username=request.user.get_username(),
                event=event,
                quizzes=quizzes
            )
            return TemplateResponse(request, "event/detail.html", context)
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
