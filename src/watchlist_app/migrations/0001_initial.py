# Generated by Django 4.1.2 on 2023-05-19 10:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('date_released', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('avg_rating', models.FloatField(default=0)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=250)),
                ('url', models.URLField()),
            ],
            options={
                'unique_together': {('name', 'url')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchlist_app.media')),
                ('the_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='watchlist_app.streamplatform'),
        ),
    ]
