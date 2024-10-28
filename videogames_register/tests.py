from django.contrib.auth.models import User
from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse
from django.contrib.auth.models import Permission
from .models import Genre, VideoGame
from django.utils import timezone
from .forms import VideogameForm

# Create your tests here.


class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(title="Action")

    def test_genre_creation(self):
        self.assertEqual(self.genre.title, "Action")
        self.assertTrue(isinstance(self.genre, Genre))
        self.assertEqual(str(self.genre), self.genre.title)

class VideoGameModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(title="Adventure")
        self.videogame = VideoGame.objects.create(
            title="The Legend of Django",
            release_date=timezone.now().date(),
            description="An epic adventure game built with Django.",
            genre=self.genre
        )

    def test_videogame_creation(self):
        self.assertEqual(self.videogame.title, "The Legend of Django")
        self.assertEqual(self.videogame.genre.title, "Adventure")
        self.assertTrue(isinstance(self.videogame, VideoGame))



class VideogameFormTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(title="Strategy")

    def test_valid_form(self):
        data = {
            'title': 'Chess Master',
            'release_date': '2023-01-01',
            'description': 'A strategy game.',
            'genre': self.genre.id,
        }
        form = VideogameForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'title': '',
            'release_date': '',
            'description': '',
            'genre': '',
        }
        form = VideogameForm(data=data)
        self.assertFalse(form.is_valid())






class VideogameListViewTest(TestCase):
    def setUp(self):
        # Create a user and log in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Assign view permission for VideoGame to the user
        permission = Permission.objects.get(codename='view_videogame')
        self.user.user_permissions.add(permission)

        # Create a genre and a video game
        self.genre = Genre.objects.create(title="Puzzle")
        self.videogame = VideoGame.objects.create(
            title="Brain Teaser",
            release_date=timezone.now().date(),
            description="A challenging puzzle game.",
            genre=self.genre
        )

    def test_videogame_list_view(self):
        # Send a GET request to the list view
        response = self.client.get(reverse('videogame_list'))
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check that the correct template was used
        self.assertTemplateUsed(response, 'videogames_register/videogame_list.html')
        # Check that the response contains the video game title
        self.assertContains(response, "Brain Teaser")
