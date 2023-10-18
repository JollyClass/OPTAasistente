# OPTA (Un Sistema Muy Inteligente)

#### aunque no tan inteligente como en la película de Iron Man o la serie de Labs rats
#### Seamos honestos, no es tan inteligente como en la película o Serie.

## construido con

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## Bendito git jsjs
## Características

Puede realizar muchas cosas interesantes, algunas de ellas son:

Saludar al usuario
Decir la hora y la fecha actual
Abrir aplicaciones/software
Abrir cualquier sitio web
Informar sobre el clima de cualquier ciudad
Abrir la ubicación de cualquier lugar y decir la distancia entre tu ubicación y el lugar consultado
Mostrar el estado actual de tu sistema (Uso de RAM, estado de la batería, uso de la CPU)
Informar sobre tus próximos eventos (Google Calendar)
Dar información sobre cualquier persona (a través de Wikipedia)
Buscar cualquier cosa en Google
Reproducir cualquier canción en YouTube
Leer los titulares principales (a través de Cnn)
Reproducir música
Enviar correos electrónicos (con asunto y contenido)
Calcular cualquier expresión matemática (por ejemplo, Opta, calcula x + 135 - 234 = 345)
Responder a cualquier pregunta genérica (a través de Wolframalpha)
Tomar notas importantes en el Bloc de notas
Contar un chiste al azar
Decir tu dirección IP
Cambiar la ventana activa
Tomar capturas de pantalla y guardarlas con un nombre de archivo personalizado
Ocultar todos los archivos en una carpeta y hacerlos visibles nuevamente

## API Keys
Para ejecutar este programa, necesitarás un conjunto de claves de API. Registra tu clave de API haciendo clic en los siguientes enlaces:

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Wolframalpha](https://www.wolframalpha.com/)
- [Google Calendar API](https://developers.google.com/calendar/auth)
  
## Instalación

- Make a config.py file and include the following in it:
    ```weather_api_key = "<your_api_key>"
    email = "<your_email>"
    email_password = "<your_email_password>"
    wolframalpha_id = "<your_wolframalpha_id>"
- Copia el archivo config.py en la carpeta OPTA>config folder
- Para activar el entorno en windows (powershell), usa ``` asistente_venv\Scripts\activate ``` en cmd ```asistente_venv/Scripts/activate.bat```
- Navega hasta el directorio del proyecto
- Instala todas las dependencias escribiendo ``` pip install -r requirements.txt ```
- activar las politicas en el cmd con permisos de administrador ```Set-ExecutionPolicy Unrestricted -Force```
- Instala PyAudio desde el archivo wheel siguiendo las instrucciones  [here](https://stackoverflow.com/a/55630212)
- Ejecuta el programa con ``` python main.py ```
- Listo

## estructura del código


    ├── driver
    ├── Opta                     # Carpeta principal para las características 
    │   ├── config           # Contiene todas las claves secretas de las API
    │   ├── features        # Todas las funcionalidades de OPTA
    │   └── utils                    # Imágenes de la GUI
    ├── __init__.py       # Definición de las funciones de las características
    ├── gui.ui              # Archivo GUI (en formato .ui)
    ├── main.py             # Programa principal de Opta
    ├── requirements.txt    # Todas las dependencias del programa

- La estructura del código es bastante simple. El código está completamente modularizado y es altamente personalizable.
Para agregar una nueva característica:
Crea un nuevo archivo en la carpeta de características, escribe la función de la característica que deseas incluir.
Agrega la definición de la función en init.py
Agrega los comandos de voz a través de los cuales deseas invocar la función
-No me acuerdo en que libro explicaban esto para estructurar el código pero esta en la biblioteca, igual creo que ustedes 2 ya vieron esto

Asegúrense de que cualquier dependencia de instalación o compilación se elimine antes del final de la capa al realizar una compilación.

Actualicen README.md con detalles de los cambios en la interfaz, esto incluye nuevas variables de entorno, puertos expuestos, ubicaciones de archivos útiles y parámetros de contenedor.

ah, lo de la licencia es por que use parte de códigos de algunos repositorios que vi ya que nos servian, tons esa licencia es para temas del copyright

- Toca revisar bien las importaciones por que las marca como exepciones

## a mejorar en un futuro
-Las conversaciones generalizadas pueden hacerse posibles mediante la  incorporación del Procesamiento del Lenguaje Natural.
-La GUI se puede hacer más agradable a la vista y funcional.
-Se pueden agregar más funcionalidades.