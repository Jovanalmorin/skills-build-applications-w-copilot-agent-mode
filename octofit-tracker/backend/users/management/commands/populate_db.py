from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from teams.models import Team
from activities.models import Activity
from workouts.models import Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spiderman', 'email': 'spidey@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        marvel_users = [User.objects.create_user(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create_user(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='Team DC')
        dc_team.members.set(dc_users)

        # Create activities
        Activity.objects.create(user=marvel_users[0], type='Running', duration=30, distance=5)
        Activity.objects.create(user=dc_users[0], type='Cycling', duration=45, distance=15)

        # Create workouts
        Workout.objects.create(user=marvel_users[1], date='2024-01-01', exercises={'pushups': 50, 'situps': 100}, notes='Great session!')
        Workout.objects.create(user=dc_users[1], date='2024-01-02', exercises={'squats': 80, 'lunges': 60}, notes='Intense workout!')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
