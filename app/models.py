from django.db import models

# Create your models here.
class Games(models.Model):
    game_n=models.CharField(max_length=100,primary_key=True)      
    
    def __str__(self):
        return self.game_n
class Player(models.Model):
    game_n=models.ForeignKey(Games,on_delete=models.CASCADE)
    player_n=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.player_n
    
    
class Location(models.Model):
    player_n=models.ForeignKey(Player,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    
    def __str__(self):
        return self.city