# Generated by Django 3.1.4 on 2021-08-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20210811_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]