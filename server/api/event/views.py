from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Q

from .models import Event
from ..users.models import User
from .serializers import EventSerialiser, CreateEventSerializer, EditEventSerializer


@api_view(["POST"])
def create_event(request):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=401)
    else:
        serialiser = CreateEventSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=200)
        else:
            return Response(serialiser.errors, status=400)


@api_view(["GET"])
def get_events(request):
    if request.user.is_authenticated is True:
        if (request.user.team_id is not None):
            events = Event.objects.filter((Q(is_public=True) | Q(team_id=request.user.team_id)) & Q(is_archived=False))
            team_serializer = EventSerialiser(events, many=True)
            return Response(team_serializer.data)
        else:
            events = Event.objects.filter(Q(is_public=True) & Q(is_archived=False))
            serializer = EventSerialiser(events, many=True)
            return Response(serializer.data)
    else:
        events = Event.objects.filter(Q(is_public=True) & Q(is_archived=False))
        limited_serializer = EventSerialiser(events, many=True)
        return Response(limited_serializer.data)


@api_view(["GET"])
def get_event(request, event_id):
    if request.user.is_authenticated is True:
        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            return Response("Event does not exist", status=404)
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response("User does not exist", status=404)
        if event in list(user.users_events.all()):
            serializer = EventSerialiser(event)
            return Response(serializer.data)
        else:
            return Response("User is not authorised to view this event", status=403)


@api_view(["PUT"])
def update_event(request, event_id):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=401)
    else:
        if request.user.team_admin is False:
            return Response("User is not authorised to update an event", status=403)
        else:
            event = Event.objects.get(event_id=event_id)
            if request.user.team_id == event.team_id:
                if event.is_public is False:
                    serializer = EditEventSerializer(instance=event, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=200)
                    else:
                        return Response(serializer.errors, status=400)
                else:
                    return Response("Event is not private", status=403)
            else:
                return Response("User is not authorised to update this event", status=403)


@api_view(["DELETE"])
def delete_event(request, event_id):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=401)
    else:
        if request.user.team_admin is False:
            return Response("User is not authorised to update an event", status=403)
        else:
            event = Event.objects.get(event_id=event_id)
            if request.user.team_id == event.team_id:
                if event.is_public is False:
                    event.delete()
                    return Response("Event successfully deleted", status=200)
                else:
                    return Response("Event is not private", status=403)
            else:
                return Response("User is not authorised to update this event", status=401)
