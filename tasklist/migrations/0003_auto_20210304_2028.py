# Generated by Django 3.1.7 on 2021-03-04 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='tasklist.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
