# Generated by Django 4.0.3 on 2022-04-21 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qforum', '0009_alter_thread_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='qforum.reply'),
        ),
    ]
