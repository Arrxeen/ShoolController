# Generated by Django 5.1 on 2024-08-18 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolcontrol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolcontrol.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolcontrol.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolcontrol.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolcontrol.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolcontrol.teacher')),
            ],
        ),
    ]
