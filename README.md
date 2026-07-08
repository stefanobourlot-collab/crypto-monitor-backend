# 🚀 Crypto Monitor Backend

Un sistema backend robusto desarrollado con **Django** y **Django REST Framework** para el seguimiento y monitoreo de criptomonedas en tiempo real. El sistema cuenta con una arquitectura de tareas asincrónicas en segundo plano utilizando **Django Q2** para consumir APIs externas sin bloquear la experiencia del usuario.

## 🛠️ Tecnologías utilizadas
* **Python 3.14+**
* **Django 6.0+** (Framework web principal)
* **Django REST Framework** (Creación de la API interactiva)
* **Django Q2** (Cluster para procesamiento de tareas en segundo plano)
* **Requests** (Cliente HTTP para integración con APIs externas)
* **SQLite** (Base de datos local por defecto)

## 📦 Características principales
1. **API REST Interactiva:** Endpoints dedicados para la gestión de activos (`/api/assets/`) y alertas de precios configurables (`/api/alerts/`).
2. **Tareas de Fondo (Background Workers):** Integración con un cluster asincrónico que procesa colas de trabajo fuera del ciclo de solicitud/respuesta del servidor web.
3. **Sincronización con CoinGecko:** Consumo automatizado de la API pública de CoinGecko para mantener actualizadas las cotizaciones de mercado en vivo.

## 🚀 Cómo ejecutar el proyecto localmente

### 1. Clonar el repositorio e ingresar
```bash
git clone [https://github.com/stefanobourlot-collab/crypto-monitor-backend.git](https://github.com/stefanobourlot-collab/crypto-monitor-backend.git)
cd crypto-monitor-backend