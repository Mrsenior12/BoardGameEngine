# Generated by Django 4.1.2 on 2022-11-10 17:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_game',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('release_year', models.PositiveIntegerField(default=2010)),
                ('avg_time', models.PositiveIntegerField(default=90)),
                ('min_player', models.PositiveSmallIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1)])),
                ('max_player', models.PositiveSmallIntegerField(default=4, validators=[django.core.validators.MaxValueValidator(15)])),
                ('minimal_age', models.PositiveIntegerField(default=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('publisher', models.CharField(default='No Data', max_length=255)),
                ('image_url', models.CharField(default='No Avaible Image', max_length=255)),
                ('time_tag', models.CharField(max_length=255)),
                ('age_tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='t_genre',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_user',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Mail', models.CharField(max_length=100, unique=True)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_user_game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_user')),
            ],
        ),
        migrations.CreateModel(
            name='t_user_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_Type', models.CharField(max_length=30, unique=True)),
                ('Activity_Timestamp', models.DateTimeField()),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_user')),
            ],
        ),
        migrations.CreateModel(
            name='t_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_number', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_user')),
            ],
        ),
        migrations.CreateModel(
            name='t_game_genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_game')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGamesAPI.t_genre')),
            ],
        ),
        migrations.CreateModel(
            name='t_friend_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_Seen', models.DateField(auto_now=True)),
                ('user1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1_id', to='BoardGamesAPI.t_user')),
                ('user2_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_id', to='BoardGamesAPI.t_user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='t_friend_list',
            constraint=models.UniqueConstraint(fields=('user1_id', 'user2_Id'), name='cant be your own friend'),
        ),
    ]
