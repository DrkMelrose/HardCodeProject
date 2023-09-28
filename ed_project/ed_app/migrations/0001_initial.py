# Generated by Django 4.2.5 on 2023-09-28 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_link', models.URLField()),
                ('duration_seconds', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_now', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessonView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_time_seconds', models.PositiveIntegerField(default=0)),
                ('is_viewed', models.BooleanField(default=False)),
                ('last_viewed_at', models.DateTimeField(blank=True, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ed_app.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='products',
            field=models.ManyToManyField(related_name='lessons', to='ed_app.product'),
        ),
    ]
