# Generated by Django 3.1.2 on 2020-11-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homeheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Klientning emaili')),
            ],
        ),
    ]
