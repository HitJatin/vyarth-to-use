# Generated by Django 3.2.12 on 2022-04-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220428_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitwaste',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]