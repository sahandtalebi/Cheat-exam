# Generated by Django 3.1.4 on 2020-12-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheatexam_question', '0002_question_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='iknow',
            field=models.BooleanField(default=True, verbose_name='جواب سوال رو بلدم'),
        ),
        migrations.AlterField(
            model_name='question',
            name='message',
            field=models.TextField(verbose_name='سوال'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('کم', 'poor'), ('زیاد', 'high')], default=False, max_length=20, verbose_name='اولویت'),
        ),
    ]
