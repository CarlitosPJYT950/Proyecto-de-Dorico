# UI del Chat

Esta es una interfaz de usuario simple para un chat que se conecta al servidor WebSocket en `ws://localhost:8765`.

## Cómo usar

1. Asegúrate de que el servidor de la API esté corriendo. Ve a la carpeta `api` y ejecuta:
   ```
   source .venv/bin/activate  # o el comando correspondiente para tu sistema
   python server.py
   ```

2. Abre el archivo `index.html` en un navegador web (por ejemplo, Chrome, Firefox).

3. La UI se conectará automáticamente al servidor WebSocket.

4. Escribe mensajes en el campo de entrada y presiona "Enviar" o Enter para enviarlos.

5. Los mensajes se mostrarán en la lista de chat y se broadcastarán a todos los clientes conectados.

## Características

- Conexión WebSocket en tiempo real.
- Interfaz simple y responsiva.
- Indicador de estado de conexión.
- Auto-scroll al último mensaje.