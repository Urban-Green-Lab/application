from . import models
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path
from .forms import QuestionForm, QuestionBankAnswerForm
from django.conf.urls import url
from .views import question_view


class MyAdminSite(AdminSite):
    index_template = "tutorial.html"
    index_title = None

    def get_urls(self):
        urls = super().get_urls()

        urls += [
            # Question Paths
            url('questions/', self.admin_view(self.question_view),
                ),
            url('questions/<str:action>',
                self.admin_view(self.question_view)),
            url('questions/<str:action>/<int:id>',
                self.admin_view(self.question_view, ),),
            url("question_view/", question_view, name="question_view")
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
