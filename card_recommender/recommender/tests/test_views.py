from django import urls
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param', [
	('home'),
	('recommendations'),
	('preferences')
])
def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200

@pytest.mark.django_db
def test_user_signup(client, user_data):
	user_model = get_user_model()
	assert user_model.objects.count() == 0
	signup_url = urls.reverse('signup')
	resp = client.post(signup_url, user_data)
	assert user_model.objects.count() == 1
	assert resp.status_code == 302