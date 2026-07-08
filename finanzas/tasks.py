import os
import django
import requests

# 1. Configuración de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nube.settings')
django.setup()

from finanzas.models import Asset
from django_q.tasks import async_task

# 2. La función que se conecta a CoinGecko
def actualizar_precios_crypto():
    print("🔄 Iniciando actualización automática de precios desde CoinGecko...")
    activos = Asset.objects.all()
    
    if not activos.exists():
        print("⚠️ No hay criptomonedas guardadas en la base de datos para actualizar.")
        return

    ids_buscar = ",".join([asset.coingecko_id for asset in activos])
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids_buscar}&vs_currencies=usd"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        for asset in activos:
            crypto_id = asset.coingecko_id
            if crypto_id in datos:
                nuevo_precio = datos[crypto_id]['usd']
                asset.current_price = nuevo_precio
                asset.save()
                print(f"✅ {asset.name} ({asset.ticker.upper()}) actualizado a: ${nuevo_precio} USD")
            else:
                print(f"❌ No se encontró precio en CoinGecko para el ID: '{crypto_id}'")
                
    except Exception as e:
        print(f"🚨 Error al conectar con CoinGecko: {e}")

# 3. EL DISPARADOR (Esto es lo que lee 'python -m finanzas.tasks')
if __name__ == "__main__":
    print("🚀 EJECUTANDO DIRECTO (SIN CLUSTER) PARA VER EL PRECIO...")
    
    # Comentamos la línea del cluster un segundo:
    # async_task(actualizar_precios_crypto)
    
    # Llamamos a la función directo:
    actualizar_precios_crypto()