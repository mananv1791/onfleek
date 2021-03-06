# Generated by Django 3.2.4 on 2021-06-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('Dress_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Dress_Number', models.IntegerField(blank=True, null=True)),
                ('Dress_Company', models.CharField(blank=True, max_length=200, null=True)),
                ('Dress_Price', models.IntegerField(blank=True, null=True)),
                ('Dress_Image', models.FileField(blank=True, upload_to='images')),
            ],
        ),
    ]
