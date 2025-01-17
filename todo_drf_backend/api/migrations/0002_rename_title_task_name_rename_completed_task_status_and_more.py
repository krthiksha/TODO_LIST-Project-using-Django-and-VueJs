# Generated by Django 4.2.14 on 2024-09-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]