# Generated by Django 4.0.3 on 2022-04-21 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qforum', '0010_alter_comment_replies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created_by',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_by',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='replied_by',
            new_name='name',
        ),
    ]
