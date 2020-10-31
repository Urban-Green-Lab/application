from django.contrib.admin.options import ModelAdmin
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
from .views import question_form, quiz_post, event_post
import datetime
from django.shortcuts import get_object_or_404, redirect
import json
import csv
from django.http import HttpResponse


class MyAdminSite(AdminSite):
    index_template = "tutorial.html"
    index_title = None
    site_header = "Urban Green Lab Admin"
    site_title = "UGL Admin Portal"
    site_url = "https://uglapp.netlify.app/"

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
            url(r"questions/delete/(?P<question_id>\d+)/",
                self.admin_view(self.question_view), name="question_delete"),
            url("question_form/", question_form, name="question_form"),
        ]

        quiz_urls = [
            url("quizzes/create", self.admin_view(self.quizzes_view),
                name="quizzes_create"),
            url("quizzes/list", self.admin_view(self.quizzes_view),
                name="quizzes_list"),
            url(r"quizzes/detail/(?P<quiz_id>\d+)/",
                self.admin_view(self.quizzes_view), name="quiz_detail"),
            url(r"quizzes/edit/(?P<quiz_id>\d+)/",
                self.admin_view(self.quizzes_view), name="quiz_edit"),
            url(r"quizzes/delete/(?P<quiz_id>\d+)/",
                self.admin_view(self.quizzes_view), name="quiz_delete"),
            url("quiz_post/", quiz_post, name="quiz_post"),
        ]

        event_urls = [
            url("events/create", self.admin_view(self.events_view),
                name="events_list"),
            url(
                "events/list",
                self.admin_view(self.events_view),
                name="events_list"
            ),
            url(r"events/detail/(?P<event_id>\d+)/",
                self.admin_view(self.events_view), name="event_detail"),
            url(r"events/delete/(?P<event_id>\d+)/",
                self.admin_view(self.events_view), name="event_delete"),
            url(r"events/edit/(?P<event_id>\d+)/",
                self.admin_view(self.events_view), name="event_edit"),
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
            app_path=request.get_full_path().split("/"),
            username=request.user.get_username(),
        )
        return TemplateResponse(request, "tutorial.html", context)

    def question_view(self, request, question_id=None):
        action = request.get_full_path().split('/')[3]
        if question_id:
            question = get_object_or_404(models.QuestionBank, pk=question_id)
        if action == "create":
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                question_form=QuestionForm(),
                answer_form_1=QuestionBankAnswerForm(prefix="a1"),
                answer_form_2=QuestionBankAnswerForm(prefix="a2"),
                answer_form_3=QuestionBankAnswerForm(prefix="a3"),
                answer_form_4=QuestionBankAnswerForm(prefix="a4"),

            )
            return TemplateResponse(request, "question/form.html", context)
        if action == "detail":
            answers = models.QuestionBankAnswer.objects.filter(
                question_bank=question)

            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                question=question,
                answers=answers
            )
            return TemplateResponse(request, "question/detail.html", context)
        if action == "list":
            questions = models.QuestionBank.objects.all()
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                questions=questions,
            )
            return TemplateResponse(request, "question/list.html", context)
        if action == "edit":
            answer_inst = question.questionbankanswer_set.all().order_by("answer")
            answers = [None, None, None, None]
            for i in range(len(answers)):
                if 4 > i:
                    answers[i] = answer_inst[i]

            # print(answers)
            def get_answer(index):
                answer = None
                if answers[index]:
                    answer = answers[index].__dict__
                    del answer["_state"]
                return answer
            answers = [
                get_answer(0),
                get_answer(1),
                get_answer(2),
                get_answer(3)
            ]
            # print(answers)
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
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
        if action == "delete":
            question.delete()
            return redirect("admin:questions_list")

    def quizzes_view(self, request, quiz_id=None, question_num=10):
        action = request.get_full_path().split('/')[3]
        if quiz_id:
            quiz = get_object_or_404(models.QuizBank, pk=quiz_id)

        if action == "create":
            questions = [None] * question_num
            questions = [QuizQuestionForm(
                prefix=f"qq{num + 1}",) for num in range(len(questions))]
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                quiz_form=QuizBankForm(),
                quiz_question_forms=questions

            )
            return TemplateResponse(request, "quiz/form.html", context)
        if action == "detail":
            questions = [
                quizquestion.question_bank
                for quizquestion in models.QuizQuestion.objects.filter(
                    quiz_bank=quiz
                )
            ]

            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                quiz=quiz,
                questions=questions,
            )
            return TemplateResponse(request, "quiz/detail.html", context)
        if action == "list":
            quizzes = models.QuizBank.objects.all()
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                quizzes=quizzes,
            )
            return TemplateResponse(request, "quiz/list.html", context)
        if action == "edit":
            question_inst = quiz.quizquestion_set.all()
            orig_questions = [None] * question_num
            for i in range(len(orig_questions)):
                if question_inst.count() > i:
                    orig_questions[i] = question_inst[i]

            def get_question(index):
                question = None
                if orig_questions[index]:
                    question = orig_questions[index].question_bank_id
                return question

            questions = [
                QuizQuestionForm(
                    prefix=f"qq{num + 1}", initial={
                        "question_bank": get_question(num)
                    }
                )
                for num in range(len(orig_questions))
            ]

            quiz_question_ids = orig_questions
            for i in range(len(quiz_question_ids)):
                if quiz_question_ids[i]:
                    quiz_question_ids[i] = quiz_question_ids[i].id

            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                quiz_form=QuizBankForm(initial=quiz.__dict__),
                quiz_question_forms=questions,
                quiz=quiz,
                quiz_question_ids=json.dumps(quiz_question_ids)
            )
            return TemplateResponse(request, "quiz/form.html", context)
        if action == "delete":
            quiz.delete()
            return redirect("admin:quizzes_list")

    def events_view(self, request, event_id=None):
        action = request.get_full_path().split('/')[3]
        if event_id:
            event = get_object_or_404(models.Event, pk=event_id)
        if action == "create":
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                event_form=EventForm(),
                event_quiz_form=EventQuizForm(),
                date=datetime.date.strftime(datetime.date.today(), "%m/%d/%Y")
            )
            return TemplateResponse(request, "event/form.html", context)
        if action == "detail":
            event = get_object_or_404(models.Event, pk=event_id)
            quizzes = [
                event_quiz.quiz
                for event_quiz in models.EventQuiz.objects.filter(
                    event=event
                )
            ]
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                event=event,
                quizzes=quizzes
            )
            return TemplateResponse(request, "event/detail.html", context)
        if action == "list":
            events = models.Event.objects.all()
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                events=events,
            )
            return TemplateResponse(request, "event/list.html", context)
        if action == "edit":
            event_quizzes = event.eventquiz_set.all()
            has_quizzes = len(event_quizzes) > 0
            context = dict(
                self.each_context(request),
                app_path=request.get_full_path().split("/"),
                username=request.user.get_username(),
                event_form=EventForm(initial=event.__dict__),
                event=event,
                event_quiz=(event_quizzes[0] if has_quizzes else None),
                event_quiz_form=EventQuizForm(
                    initial=(
                        {
                            "quiz": event_quizzes[0].quiz.id
                            if has_quizzes
                            else {}
                        }
                    )
                ),
                date=datetime.date.strftime(event.date, "%m/%d/%Y")
            )
            return TemplateResponse(request, "event/form.html", context)
        if action == "delete":
            event.delete()
            return redirect("admin:events_list")


class QuizTakerAdmin(ModelAdmin):
    """
    Display first, last name, email, event name, and event date
    Filter by event
    Select the users that should be downloaded
    Disallow add and change on this view
    """
    list_display = ['fname', 'lname', 'email', 'event', 'created_at', "date"]
    list_filter = ('event',)
    ordering = ['email', 'fname']
    actions = ['export_as_csv']

    def date(self, quiz_taker):
        return quiz_taker.event.date

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field)
                             for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected As CSV"


class QuestionAnswer():
    def __init__(self, question, answer, info_link):
        self.question = question
        self.answer = answer
        self.info_link = info_link


admin_site = MyAdminSite(name='myadmin')

# Register your models here.
admin_site.register(models.QuizTaker, QuizTakerAdmin)
