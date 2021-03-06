import datetime

from django.test import TestCase
from django.urls import reverse
from volunteer.models import VolunteerEvent
from django.utils import timezone

from django.contrib.auth.models import User


class TestIndexView(TestCase):

    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("volunteer:index"))
        self.assertRedirects(response, "/?next=/volunteer/")

    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)
        response = self.client.get(reverse("volunteer:index"))
        self.assertEqual(response.status_code, 200)

class TestCreateEventView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("volunteer:createpost"))
        self.assertRedirects(response, "/?next=/volunteer/post/")

    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)
        response = self.client.get(reverse("volunteer:createpost"))
        self.assertEqual(response.status_code, 200)


class TestEventBrowseView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("volunteer:eventbrowse"))
        self.assertRedirects(response, "/?next=/volunteer/events/")

    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)
        response = self.client.get(reverse("volunteer:eventbrowse"))
        self.assertEqual(response.status_code, 200)

class TestMyScheduleView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("volunteer:myschedule"))
        self.assertRedirects(response, "/?next=/volunteer/schedule/")

    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)
        response = self.client.get(reverse("volunteer:myschedule"))
        self.assertEqual(response.status_code, 200)

class TestDetailView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("volunteer:detail", kwargs={'pk':1}))
        self.assertRedirects(response, "/?next=/volunteer/events/1")

    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)

        VolunteerEvent.objects.create(event_title='Fun Event', event_description='This event will be really fun', event_author=user)
        event = VolunteerEvent.objects.get(event_title='Fun Event')

        response = self.client.get(reverse("volunteer:detail", kwargs={'pk':event.pk}))
        self.assertEqual(response.status_code, 200)

    def test_user_registered(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)

        VolunteerEvent.objects.create(event_title='Fun Event', event_description='This event will be really fun', event_author=user)
        event = VolunteerEvent.objects.get(event_title='Fun Event')
        event.attending.set([user.pk])

        response = self.client.get(reverse("volunteer:detail", kwargs={'pk':event.pk}))
        self.assertTrue(response.context['registered'])

    def test_user_unregistered(self):
        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
        user.save()
        self.client.force_login(user=user)

        VolunteerEvent.objects.create(event_title='Fun Event', event_description='This event will be really fun', event_author=user)
        event = VolunteerEvent.objects.get(event_title='Fun Event')

        response = self.client.get(reverse("volunteer:detail", kwargs={'pk':event.pk}))
        self.assertFalse(response.context['registered'])
