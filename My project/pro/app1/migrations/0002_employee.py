# Generated by Django 3.0 on 2021-12-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('des', models.CharField(max_length=20)),
            ],
        ),
    ]