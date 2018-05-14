# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-18 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToxicComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.CharField(max_length=255)),
                ('post_id', models.CharField(max_length=255)),
                ('comment_id', models.CharField(max_length=255)),
                ('comment_text', models.TextField()),
                ('toxicity', models.IntegerField(choices=[(0, 'Toxic'), (1, 'Not Toxic')])),
            ],
        ),
    ]