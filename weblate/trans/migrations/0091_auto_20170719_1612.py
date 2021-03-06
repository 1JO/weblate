# -*- coding: utf-8 -*-
# Generated by Django 1.11.2.dev20170512010505 on 2017-07-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0090_auto_20170718_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproject',
            name='commit_pending_age',
            field=models.IntegerField(default=24, help_text='Time in hours after which any pending changes will be committed to the VCS.', verbose_name='Age of changes to commit'),
        ),
        migrations.AddField(
            model_name='subproject',
            name='push_on_commit',
            field=models.BooleanField(default=True, help_text='Whether the repository should be pushed upstream on every commit.', verbose_name='Push on commit'),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='file_format',
            field=models.CharField(choices=[('aresource', 'Android String Resource'), ('auto', 'Automatic detection'), ('csv', 'CSV file'), ('csv-simple', 'Simple CSV file'), ('csv-simple-iso', 'Simple CSV file (ISO-8859-1)'), ('joomla', 'Joomla Language File'), ('json', 'JSON file'), ('json-nested', 'JSON nested structure file'), ('php', 'PHP strings'), ('po', 'Gettext PO file'), ('po-mono', 'Gettext PO file (monolingual)'), ('poxliff', 'XLIFF Translation File with PO extensions'), ('properties', 'Java Properties (ISO-8859-1)'), ('properties-utf16', 'Java Properties (UTF-16)'), ('properties-utf8', 'Java Properties (UTF-8)'), ('resx', '.Net resource file'), ('ruby-yaml', 'Ruby YAML file'), ('strings', 'OS X Strings'), ('strings-utf8', 'OS X Strings (UTF-8)'), ('ts', 'Qt Linguist Translation File'), ('webextension', 'WebExtension JSON file'), ('xliff', 'XLIFF Translation File'), ('yaml', 'YAML file')], default='auto', help_text='Automatic detection might fail for some formats and is slightly slower.', max_length=50, verbose_name='File format'),
        ),
    ]
