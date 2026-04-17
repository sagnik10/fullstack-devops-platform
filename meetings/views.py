from django.shortcuts import render
from .services import create_zoom_meeting

def start_meeting(request):

    meeting=create_zoom_meeting("DevOps Class")

    return render(request,"meetings/meeting.html",{"meeting":meeting})
