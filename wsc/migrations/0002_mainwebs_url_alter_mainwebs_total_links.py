# Generated by Django 4.2 on 2023-04-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainwebs',
            name='url',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainwebs',
            name='total_links',
            field=models.CharField(blank=True, default='in progress', null=True),
        ),
    ]
