from django.db import models
import datetime
from ..users.models import User
from ..team.models import Team
from ..event.models import Event
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


class Mileage(models.Model):
    mileage_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kilometres = models.FloatField()
    date = models.DateField(default=datetime.date.today)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.id} {self.kilometres} {self.date}'


@receiver(pre_save, sender=Mileage)
def on_change(sender, instance, **kwargs):
    if instance.event:
        event = Event.objects.get(event_id=instance.event.event_id)
        event.total_mileage += instance.kilometres
        event.save()
    if instance.mileage_id:  # updating rather than creating
        previous = Mileage.objects.get(mileage_id=instance.mileage_id)
        instance.user.total_mileage += (instance.kilometres - previous.kilometres)
        instance.user.save()
        if instance.user.team_id:
            instance.user.team_id.total_mileage += (instance.kilometres - previous.kilometres)
            instance.user.team_id.save()
    else:  # creating than updating
        user = User.objects.get(id=instance.user.id)
        user.total_mileage += instance.kilometres
        user.save()
        if instance.user.team_id:
            instance.user.team_id.total_mileage += instance.kilometres
            instance.user.team_id.save()


@receiver(post_delete, sender=Mileage)
def on_delete(sender, instance, **kwargs):
    if instance.event:
        event = Event.objects.get(event_id=instance.event.event_id)
        event.total_mileage -= instance.kilometres
        event.save()
    if instance.user.team_id:
        instance.user.team_id.total_mileage -= instance.kilometres
        instance.user.team_id.save()
    instance.user.total_mileage -= instance.kilometres
    instance.user.save()
