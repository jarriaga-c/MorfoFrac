# MorfoFrac

Este programa permite realizar un conteo de cajas, técnica que permite estimar la dimension fractal de una figura de tipo poligonal de una o varias piezas, contenida en el archivo sobre el cual se corre el proceso. El programa entrega 6 archivo SHP con sus respectivos archivos axesorios, el primero de los cuales contiene la caja cuadrada mínima, es decir, el mínimo cuadro que contiene toda la figura analizada. Posteriormente se generan otros cinco archivos, el primero de estos divide al cuadro del primer archivo en cuatro cuadrados iguales dentro, el siguiente, 6 cuadrados de la mitad de largo de los anteriores, que caben dentro de estos, y así suscesivamente. Despues de generar los archivos, el programa entrega un listado que indica el número de cuadros de cada archivo, y el número de cuadros ocupados de cada dimensión con lo cual se puede estimar fuera del programa QGIS, la línea de regresión cuya pendiente es la dimensión fractal.

El programa ha sido desarrollado en la Unidad de Geotecnología Infraestructura Transporte y Sustentabilidad del Instituto de Geografía de la UNAM en México.

En el participaron Jair Arriaga Carbajal y Tonatiuh Suárez Meaney bajo la dirección de Luis Chías Becerril.

Actualmente el complemento se encuentra en las primeras etapas del desarrollo por lo que sigue en proceso de admisión por Qgis, debido a esto el complemento se tiene que instalar a mano.

Pasos de instalación

Descargar el código de github
Copiar la carpeta “fractaliadj”
Pegar la carpeta copiada en el ruta “C:\Users\”usuarios”\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins”
Buscar complemento instalado en Qgis en la caja de herramientas con el nombre "Fractalidad".
En caso de no aparecer favor de ir a complementos / administrar e instalar complementos / instalado
Buscar Morfofrac y activarlo.

Una vez que se el programa ha devuelto la relación de número de cuadros utilizados, Se pega esa línea en el archivo anexo de Excel, en los cuadros amarillos, etnonces en el cuadro azul aparecerá la dimensión rfactal estimada. 

En la próxima versión el mismo programa dará la dimensión.
