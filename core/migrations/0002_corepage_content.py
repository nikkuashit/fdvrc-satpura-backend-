# Generated by Django 3.2.11 on 2022-02-10 18:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='corepage',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
