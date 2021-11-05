# Timbre intercomunicador de video rápido 

## Introducción 
```
El proyecto en el que se basa este trabajo es un timbre intercomunicador con audio y video, el cual tiene la finalidad de notificar a la persona que esta dentro de la casa, oficina o cualquier otro lugar quien esta afuera, para posteriormente permitirle el ingreso, en palabras del autor: 
> El proyecto no es muy complicado, solo necesitas algunos conocimientos básicos de soldadura.
> La buena noticia es que todos los componentes caben en una pequeña carcasa.
```
![Imagen](https://i.all3dp.com/cdn-cgi/image/fit=cover,w=1000,gravity=0.5x0.5,format=auto/wp-content/uploads/2021/01/20120128/Video-Doorbell-Raspberry-Pi.jpeg)

## Procedimiento 

Para la realización de este proyecto se necesitan materiales de distintos tipos:

1.  **Componentes de Hardware**

Rasberry Pi 3 Modelo B | Tarjeta de memoria micro SD
-----------------------| --------------------------
Fuente de alimentación para Rasberry Pi 3 | Estuche de plastico con apertura para modulo de camara 
Modulo de camara de video para Pi | Altavoz con amplificador incorporado 
Cable de 3 pines a hembra para altavoz | Microfono mini USB 
Interruptor de boton de encendido y apagado | Cables de puente 

2. **Aplicaciones de software y servicios en línea**

* SDK de Seajei
* Estiramiento  raspbian
*  Generador de imagenes Rasberry Pi

3. **Herramientas manuales y máquinas de fabricación**

* Kit de soldador 

La creación de el proyecto ya con todos nuestros materiales se realiza en 10 pasos:

**_Paso uno: preparar y ensamblar todos los componentes de hardware_**

Se toma la caja de plastico y se hacen los agujeros donde van a ir cada una de las piezas como se muestra en la siguiente imagen: 

![Imagen 2](https://hackster.imgix.net/uploads/attachments/1232973/01-holediagram_xm6I2h18WC.png?auto=compress%2Cformat&w=740&h=555&fit=max)

Como opción personal se puede pintar o dejar trasparente, posteriormente se preparan los cables de altavoces cortandolos y volviendolos a soldar como se presenta a continuación: 

![Imagen 3](https://hackster.imgix.net/uploads/attachments/1232980/screen_shot_2020-12-16_at_4_50_06_pm_TL5waIP77m.png?auto=compress%2Cformat&w=740&h=555&fit=max)

A continuación, pele algunos cables de puente adicionales y conéctelos y suéldelos al botón, se instalan todos los componentes en la cubierta de la caja cuidando que esten en los lugares respctivos. Ahora, para la salida de audio, corte y pele otro cable de puente (macho para que se conecte con el cable hembra en el altavoz) y páselo por el orificio cerca del audio Y luego soldarlo al pin de salida de audio del conector de audio de 3,5 milímetros, en la siguiente imagen se puede ver la ubicación del pin de salida de audio **flecha roja**:

![Imagen 4](https://hackster.imgix.net/uploads/attachments/1233001/screen_shot_2020-12-16_at_4_29_13_pm_Wq9DtxUDbA.png?auto=compress%2Cformat&w=740&h=555&fit=max)

Se empuja la Rasberry Pi en la base de la carcasa y conecta todos los cables. A continuación se muestra el diagrama de los números de pin de Raspberry Pi. Conecte la alimentación del altavoz al pin n. ° 1. tierra del altavoz al n. ° 6. Botón de cables a los pines n. ° 7 y n. ° 9. Luego se cierra la tapa y se pasa al segundo paso.

![Imagen 5](https://hackster.imgix.net/uploads/attachments/1233536/pi3pins_pzmJGS7aT8.png?auto=compress%2Cformat&w=740&h=555&fit=max)

**_Paso dos: instale un sistema operativo nuevo en Raspberry Pi_**

Para su Raspberry Pi 3 (o 3+), descargue y descomprima Raspbian Stretch. Descargue e instale Raspberry Pi Imager .
Conecte un monitor con el cable HDMI y conecte un mouse y un teclado USB. Luego enciende la Raspberry Pi, Descargue e instale Raspberry Pi Imager . Conecta y formatea tu tarjeta microSD. Luego, inicie Raspberry Pi Imager. Elija un sistema operativo personalizado para instalar y navegue hasta el archivo Raspbian Stretch que descargó y descomprimió. Seleccione su tarjeta microSD y haga clic en "ESCRIBIR". Cuando haya terminado, conecte la tarjeta microSD a su Raspberry Pi. Conecte un monitor con el cable HDMI y conecte un mouse y un teclado USB. Luego enciende la Raspberry Pi.

**_Paso tres: configure Pi para que se conecte a WiFi y haga que la cámara funcione correctamente_**



## Limitaciones 

* El sistema de notificación para tu Smartphone solo se puede enviar a traves de mac 
* 

### Referencias 

[Timbre intercomunicador de video rápido](https://www.hackster.io/sneaky/fast-video-doorbell-intercom-on-raspberry-pi-63b063)
