# Generated by Django 4.2.16 on 2024-11-10 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('course_details', '0001_initial'),
        ('course_instructor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course_content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='course_details.coursecontent')),
            ],
        ),
        migrations.CreateModel(
            name='VideoProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_details.coursecontent')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('passed', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_instructor.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_take_quiz', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_details.coursecontent')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(choices=[('a', 'Option A'), ('b', 'Option B'), ('c', 'Option C'), ('d', 'Option D')], max_length=255)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='course_instructor.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='NextVideoAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_access', models.BooleanField(default=False)),
                ('current_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_video', to='course_details.coursecontent')),
                ('next_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next_video', to='course_details.coursecontent')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]