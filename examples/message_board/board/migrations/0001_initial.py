# Generated by Django 2.0.1 on 2018-01-22 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=144)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
