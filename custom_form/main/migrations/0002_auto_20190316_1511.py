# Generated by Django 2.1.5 on 2019-03-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('confirm_password', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
