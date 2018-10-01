# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-01 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Question')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Team')),
            ],
        ),
    ]
