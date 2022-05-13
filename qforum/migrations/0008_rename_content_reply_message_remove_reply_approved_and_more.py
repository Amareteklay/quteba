# Generated by Django 4.0.3 on 2022-04-21 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qforum', '0007_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='post',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='replies',
        ),
        migrations.AddField(
            model_name='reply',
            name='replied_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='status',
            field=models.IntegerField(choices=[(0, 'Waiting'), (1, 'Approved')], default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('commented_on', models.DateTimeField(auto_now_add=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('replies', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='qforum.reply')),
            ],
            options={
                'ordering': ['-commented_on'],
            },
        ),
        migrations.AddField(
            model_name='thread',
            name='comments',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='qforum.comment'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='qforum.comment'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]