# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-11 18:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 10, 11, 18, 58, 33, 795108, tzinfo=utc), verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100, unique=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 10, 11, 18, 58, 33, 789223, tzinfo=utc), verbose_name='date published')),
                ('image', models.ImageField(default='default.jpg', upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 10, 11, 18, 58, 33, 793843, tzinfo=utc), verbose_name='date published')),
                ('correct_answer', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Memorama',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question_game.Game')),
                ('num_of_pairs', models.IntegerField()),
            ],
            bases=('question_game.game',),
        ),
        migrations.CreateModel(
            name='Question_game',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question_game.Game')),
                ('time', models.IntegerField()),
            ],
            bases=('question_game.game',),
        ),
        migrations.AddField(
            model_name='question',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Game'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_game.Team'),
        ),
    ]
