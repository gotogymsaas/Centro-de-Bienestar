# Centro de Bienestar

Este proyecto combina un backend en Django con un frontend en Next.js pensado para empaquetarse como PWA mediante Capacitor.

## Requisitos
- Node.js 18+
- Python 3.10+
- PostgreSQL

## Instalación
1. Instala dependencias de Node y Python:
   ```bash
   npm install
   pip install -r requirements.txt
   ```
2. Copia `.env.example` a `.env` y completa las variables necesarias:
   - `SECRET_KEY`
   - `DB_PASSWORD`
3. Construye el frontend y copia los archivos exportados a `www/`:
   ```bash
   npm run build
   ```
4. Sincroniza las plataformas móviles con Capacitor:
   ```bash
   npx cap sync
   ```
5. Para desarrollo del frontend ejecuta:
   ```bash
   npm --prefix webapp run dev
   ```

El directorio `www/` contendrá la versión estática lista para usarse en las aplicaciones móviles.
