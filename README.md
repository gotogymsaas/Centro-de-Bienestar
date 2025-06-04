# Centro de Bienestar

Este repositorio contiene el backend y los recursos de la aplicación GoToGym.

Las carpetas `android/` e `ios/` almacenan los proyectos móviles de Capacitor.
A partir de ahora estas son las únicas rutas usadas para generar las apps.
Se eliminó el antiguo directorio `mobile/` que contenía copias de estos
proyectos.

Para compilar los proyectos móviles utiliza los comandos de Capacitor desde la
raíz del repositorio:

```bash
npx cap sync android
npx cap sync ios
```

Esto generará los archivos en `android/` e `ios/` listos para abrirse en Android
Studio o Xcode respectivamente.
