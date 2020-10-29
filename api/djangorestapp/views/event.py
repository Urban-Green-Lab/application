from django.http import HttpResponse
from ..models import Event, EventQuiz
import datetime


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

        return HttpResponse("Event created add even detail view here")
