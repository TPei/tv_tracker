# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=3, choices=[(0, '0 - grottig'), (1, '1 - schlecht'), (2, '2 - mittelmäßig'), (3, '3 - nett'), (4, '4 - gut'), (5, '5 - sehr gut'), (6, '6 - ausgezeichnet')])),
                ('message', models.CharField(max_length=200, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=1000, blank=True, null=True)),
                ('imdb_id', models.CharField(max_length=9, blank=True, null=True)),
                ('youtube_link', models.CharField(max_length=200, blank=True, null=True)),
                ('picture', models.CharField(max_length=300, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='show',
            name='tags',
            field=models.ManyToManyField(to='shows.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='show',
            field=models.ForeignKey(to='shows.Show'),
            preserve_default=True,
        ),
    ]
