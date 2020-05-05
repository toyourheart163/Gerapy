'''
init db for test
'''

import os
import sys

pwd = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(pwd))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.heroku_settings')

import django
django.setup()

from django.contrib.auth.models import User, Group

from core.models import Project, Client


if Group.objects.count() == 0:
    for name in ['visitor', 'admin']:
        Group.objects.create(name=name)

if User.objects.count() == 0:
    owner = User(username='bar')
    owner.is_superuser = True
    owner.is_staff = True
    owner.set_password('ok')
    owner.save()
    group = Group.objects.get(name='visitor')
    owner.groups.add(group)
else:
    owner = User.objects.first()

Client.objects.update_or_create(
        ip='localhost', port=6800,
        description='local', name='local',
        owner=owner, open=True)

project_path = os.path.join(BASE_DIR, 'projects')
print(Project.objects.all())
if os.path.isdir(project_path):
    files = os.listdir(project_path)
    print(files)
    for file in files:
        Project.objects.update_or_create(
            name=file,
            owner=owner,
            open=True
        )
