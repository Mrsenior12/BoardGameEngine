
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.utils.translation import gettext_lazy as _
from django.conf import settings


#todo: dodaj te modele jako crudy w panelu administratora zeby moc miec dostep "z reki"
#https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
#wszystkie modele w adminie

# Create your models here.


class t_user(models.Model):
    id = models.BigAutoField(primary_key=True)
    Username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    Mail = models.CharField(max_length=100, unique=True, null=False, blank=False)
    Password = models.CharField(max_length=50, null=False, blank=False)


# "%(app_label)s_%(class)user1_id"
class t_friend_list(models.Model):
    #user1_id = models.ForeignKey(t_user,
    #                             null=False,
    #                             blank=False,
    #                             on_delete=models.CASCADE,
    #                             related_name="user1_id")
    user2_Id = models.ForeignKey(t_user,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE,
                                 related_name="user2_id")
    user1_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #user2_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    Last_Seen = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            # Ensures constraint on DB level, raises IntegrityError (500 on debug=False)
            #models.CheckConstraint(check=~Q((F('user1_id') == F('user2_id'))), name='check_same_user_IDs'), #django upraszcza to sb do TRUE albo false
            #bo rozumie to jako to samo pole, tzreba dac funkcje z importa gdzies z zewnatrz, albo w BD recznie to dodac
            models.UniqueConstraint(fields=['user1_id', 'user2_Id'], name="cant be your own friend")
        ]

class t_user_activity(models.Model):
    User_Id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #models.ForeignKey(t_user, on_delete=models.CASCADE)
    Activity_Type = models.CharField(max_length=30, unique=True, null=False, blank=False)
    Activity_Timestamp = models.DateTimeField()

class t_genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(max_length=255,
                                  unique=True,
                                  null=False,
                                  blank=False)

class t_game(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255,
                            unique=True,
                            null=False,
                            blank=False)
    game_designer = models.CharField(max_length=255,
                                    null=False,
                                    blank=False)
    game_description = models.TextField(max_length=2000,
                                    null=True,
                                    blank=True)
    release_year = models.PositiveIntegerField(default=2010)
    min_game_time = models.PositiveIntegerField()
    max_game_time = models.PositiveIntegerField()
    avg_time = models.PositiveIntegerField(default=90)

    min_player = models.PositiveIntegerField(default=2,
                                                  validators=[
                                                      MinValueValidator(1)
                                                  ])

    max_player = models.PositiveIntegerField(default=4,
                                                  validators=[
                                                      MaxValueValidator(15),
                                                  ])
    suggested_players = models.PositiveIntegerField()
    minimal_age = models.PositiveIntegerField(default=12,
                                                validators=[
                                                    MinValueValidator(0)])
    
    suggested_age = models.PositiveIntegerField()
    publisher = models.CharField(default="No Data",max_length=255)                                                                                                
    image_url = models.CharField(default="No Avaible Image",max_length=255)

"""
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(min_player__lt=F('max_player')),
                name='min_player_lower_than_max')
        ]

    def _str_(self):
        return self.title
"""

class t_game_genre(models.Model):
    game_id = models.ForeignKey(t_game,
                                on_delete=models.CASCADE)
    genre_id = models.ForeignKey(t_genre,
                                 on_delete=models.CASCADE)


class t_review(models.Model):
    game_id = models.ForeignKey(t_game,
                                on_delete=models.CASCADE)

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    #models.ForeignKey(t_user,
    #                            on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    review_number = models.DecimalField(
        null=False,
        blank=False,
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])

    description = models.TextField(max_length=1000,
                                    null=True,
                                    blank=True)


class t_user_game(models.Model):
    #user_id = models.ForeignKey(t_user,
    #                            on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    game_id = models.ForeignKey(t_game,
                                on_delete=models.CASCADE)