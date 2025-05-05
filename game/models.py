from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    player_white = models.ForeignKey(User, on_delete=models.CASCADE, related_name='white_games')
    player_black = models.ForeignKey(User, on_delete=models.CASCADE, related_name='black_games')
    moves = models.TextField(blank=True, null=True)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return f"Game {self.id} - {self.player_white} vs {self.player_black}"