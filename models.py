from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    """Representa la criptomoneda que estamos monitoreando (ej: bitcoin, ethereum)"""
    coingecko_id = models.CharField(max_length=50, unique=True, help_text="ID oficial en la API de CoinGecko (ej: 'bitcoin')")
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    current_price = models.DecimalField(max_digits=18, decimal_places=4, default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ticker.upper()}) - ${self.current_price}"

class PriceAlert(models.Model):
    """La regla de alerta creada por el usuario"""
    CONDITION_CHOICES = [
        ('ABOVE', 'Por encima de'),
        ('BELOW', 'Por debajo de'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='alerts')
    target_price = models.DecimalField(max_digits=18, decimal_places=4)
    condition = models.CharField(max_length=5, choices=CONDITION_CHOICES)
    is_active = models.BooleanField(default=True, help_text="Indica si la alerta está operativa")
    is_triggered = models.BooleanField(default=False, help_text="Evita que se envíen múltiples mails repetidos si el precio se mantiene")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alerta {self.user.username}: {self.asset.ticker} {self.condition} ${self.target_price}"