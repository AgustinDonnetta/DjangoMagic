from django.db import models
from django.conf import settings
from PIL import Image

def get_upload_player(instance, filename):
    return '/'.join([settings.FILES_PATH, "player", str(instance.id), filename])

class Player(models.Model):
    full_name = models.CharField(max_length=40)
    DNI = models.IntegerField()
    born_date = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to=get_upload_player)
    is_active = models.BooleanField(default=True) 
    
    def save(self):
        super().save()
    
        try:   
            img = Image.open(self.image.path)

            if img.height > 300 or img.height > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            pass

    def __str__(self):
        return self.full_name

class Match(models.Model):
    status_choices = (("ongoing", "ongoing"),
                    ("cancelled", "cancelled"),
                    ("finished","finished"),
                    )
    player_1 = models.ForeignKey(Player,related_name='Jugador_1', on_delete=models.PROTECT)
    player_2 = models.ForeignKey(Player,related_name='Jugador_2',on_delete=models.PROTECT)
    date = models.DateField()
    winner = models.ForeignKey(Player,related_name='Ganador', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True) 

    status_2 = models.CharField(choices=status_choices, max_length=40, default="ongiong") 

    def __str__(self):
        return self.player_1.full_name


class Turn(models.Model):
    attack_choices = (("Yes", "Yes"),
                    ("No", "No"),
                    )
    match = models.ForeignKey(Match,related_name='Match', on_delete=models.PROTECT)
    turn_number = models.IntegerField()
    player = models.ForeignKey(Player,related_name='Player', on_delete=models.PROTECT)
    play_land = models.BooleanField(default=False)
    play_creatures = models.CharField(max_length=15)
    play_another_thing = models.CharField(blank=True, max_length=20)
    attack = models.CharField(choices=attack_choices, max_length=10)
    player_1_life = models.IntegerField()
    player_2_life = models.IntegerField()
