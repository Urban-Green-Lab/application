from . import models
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.urls import path


class MyAdminSite(AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('my_view/', self.admin_view(self.my_view))
        ]
        return urls

    def my_view(self, request):
        print(request.user, "*********************")
        context = dict(
            self.each_context(request),
            title=('Twsdfsrsr'),
            app_path=None,
            username=request.user.get_username(),
        )
        return TemplateResponse(request, "sometemplate.html", context)

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

admin_site = MyAdminSite(name='myadmin')
admin_site.site_url = None
# Register your models here.

admin_site.register(models.EventQuiz)
admin_site.register(models.Event)
admin_site.register(models.QuestionBankAnswer)
admin_site.register(models.QuestionBank)
admin_site.register(models.QuizBank)
admin_site.register(models.QuizQuestion)
admin_site.register(models.QuizTaker)

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "date", "active")
    list_filter = ("name", "date")
    actions = ["export_as_csv"]
