# Generated by Django 4.2.6 on 2024-01-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_value',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_boolean',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(blank=True, default='project_manager/no_image.jpg', upload_to='upload/'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_longtext',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]