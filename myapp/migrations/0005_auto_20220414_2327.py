# Generated by Django 3.2.12 on 2022-04-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_collectwaste_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitwaste',
            name='number',
        ),
        migrations.AddField(
            model_name='submitwaste',
            name='fullname',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
