from django.db import models

# Create your models here.
class Games(models.Model):
    gamen=models.CharField(max_length=100,primary_key=True)      
    
    def __str__(self):
        return self.gamen
class Player(models.Model):
    gamen=models.ForeignKey(Games,on_delete=models.CASCADE)
    playern=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.playern
    
    
class Location(models.Model):
    playern=models.ForeignKey(Player,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    
    def __str__(self):
        return self.city