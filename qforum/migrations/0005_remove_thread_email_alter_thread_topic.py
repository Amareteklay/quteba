# Generated by Django 4.0.3 on 2022-04-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qforum', '0004_alter_thread_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='email',
        ),
        migrations.AlterField(
            model_name='thread',
            name='topic',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]