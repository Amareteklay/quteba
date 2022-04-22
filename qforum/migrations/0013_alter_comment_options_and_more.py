# Generated by Django 4.0.3 on 2022-04-22 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qforum', '0012_rename_comment_comment_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commented_on',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qforum.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='qforum.thread'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
