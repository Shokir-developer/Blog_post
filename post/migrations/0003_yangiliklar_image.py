# Generated by Django 4.0.2 on 2022-02-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_yangiliklar_main_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='image',
            field=models.ImageField(null=True, upload_to='imaegs'),
        ),
    ]
