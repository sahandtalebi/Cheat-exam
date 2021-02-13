# Generated by Django 3.1.4 on 2020-12-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheatexam_question', '0024_remove_question_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, default='s', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='message',
            field=models.TextField(verbose_name='سوال'),
        ),
    ]
