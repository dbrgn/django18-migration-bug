# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='John',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=42)),
            ],
        ),
        migrations.AddField(
            model_name='john',
            name='consumed_food',
            field=models.ManyToManyField(related_name='eater', to='debug.Spam', blank=True),
        ),
    ]
