# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_tarefas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tarefas',
            new_name='Tarefa',
        ),
    ]