# Generated by Django 4.0.3 on 2022-04-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(default='media/profileimages/default.jpg', upload_to='media/profileimages')),
                ('bio', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('born_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
