# Generated by Django 4.2.16 on 2024-11-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('course_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='course_details.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_courses', to='main.profile')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
