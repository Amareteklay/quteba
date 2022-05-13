# Generated by Django 4.0.3 on 2022-04-19 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qforum', '0005_remove_thread_email_alter_thread_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thread',
        ),
        migrations.AddField(
            model_name='thread',
            name='replies',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_reply', to='qforum.post'),
        ),
    ]