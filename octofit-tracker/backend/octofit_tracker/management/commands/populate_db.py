from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Cancella dati esistenti
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crea team
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crea utenti
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)

        # Crea attività
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Crea workout
        Workout.objects.create(user=tony, name='Iron Endurance', description='HIIT', duration=40)
        Workout.objects.create(user=bruce, name='Bat Strength', description='Strength', duration=60)

        # Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=80)
        Leaderboard.objects.create(user=bruce, points=90)
        Leaderboard.objects.create(user=clark, points=95)

        self.stdout.write(self.style.SUCCESS('Database popolato con dati di test!'))
