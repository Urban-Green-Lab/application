from django.http import HttpResponse
from ..models import Event, EventQuiz, QuizBank
import datetime
from django.shortcuts import redirect, get_object_or_404


def event_post(request):
    if request.method == "POST":
        data = request.POST

        date_obj = datetime.datetime.strptime(data.get("date"), "%m/%d/%Y")
        date_str = datetime.date.strftime(date_obj, "%Y-%m-%d")
        event = Event.objects.create(
            name=data.get("name"),
            active=True if data.get("active") else False,
            child_mode=True if data.get("child_mode") else False,
            date=date_str
        )

        quiz = get_object_or_404(QuizBank, pk=int(data.get("quiz")))
        EventQuiz.objects.create(
            event=event,
            quiz=quiz
        )

        return redirect('admin:event_detail', event_id=event.id)


def event_detail(request, event_id=None):
    if event_id:
        event = get_object_or_404(Event, pk=event_id)
        return HttpResponse(f"Quiz {event_id}")
