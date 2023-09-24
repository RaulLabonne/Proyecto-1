
## Capy Weather

### Proposito
Se deberá entregar una aplicación gráfica la cual acepte como entrada, un ticket o el nombre
de la ciudad a la cual se esta interesado en conocer el clima. La entrada debe ser capaz de aceptar
errores, por ejemplo: Monterye, Montery, Monterey y MTY, cada uno de estos deberá contestar
con el clima de Monterey.

### Dependencias nesesarias:
* Pandas
* Flask
* requests

>:warning:
>la instalacion de librerias y como correr el programa estaran al fondo del Readme

### Desarrollo:
La primer problematica a enfretarnos seria la de saber como conseguir la informacion del clima de una ciudad dada, para esto se utilizo los servicios de OpenWeather[^1], esta es una empresa que pone a nuestra disposicion una API a la cual llamas con unas coordenadas y una llave, esta devuelve el clima de las coordenadas proporcionadas.
>:key:
> nesesitas una API key valida proporcionada por OpenWeather, en su pagina estan las instrucciones para conseguirla, por motivos obvios no la podemos proporsionar nosotros.

Ya que se posee la una forma de acceder al clima de cualquier parte del mundo, se tendra que ver como es que se obtienen los datos, para esto se nos proporciono un dataset(en formato csv), de la cual sacar los tickets y las coordenadas de las ciudades, asi pues ya tenemos la base de datos. Sin embargo, como el programa puede recibir el IATA code de un aeropuerto, y ademas el nombre de la ciudad donde se encuentra, se contara con un dataset independiente en el que se almacena el IATA code, el nombre de la ciudad y las coordenadas de la misma (tambien en formato csv).

Como contamos con archivos csv en los cuales tenemos almacenada la informacion, una forma de poder leerlos y hacer busquedas en el de forma relativamente simple, sera utilizando la libreria de pandas, esta nos permite leer datasets en diversos formatos y manipularlos de forma sencilla
para su implementacion basta con leer la documentacion [^2]. Asi pues, ya es posible leer los datasets proporcionados y resactar de ellos la informacion que nesitamos.

Ahora bien, ya tenemos como conseguir las coordenadas nesesarias para el clima, es nesesario buscar con una forma de llamar a la API con los datos correspondentes para conseguir la información que se requeire. para lograr esto de una forma en la quie sea sencillo capturar posibles errores a la hora de hacer la peticion, y que ademas nos de la informacion en un formato facil de manipular, de desidio por usar la libreria de requests[^3], ya que esta solo requiere como argumento una url y a partir del objeto instanciado es facil verificar el estatus que mando el servidor de la API y recuperar la informacion que este regresa en formato json es muy facil.

Como se sigue el patron de diselño MVC (Modelo Vista controlador) y ya tenemos toda la parte del modelo cubierta, es nesesario determinar con que se realizara la parte de vista (ya que esto determina como se hara el controlador que comunicara ambas partes), asi pues basado en facilidad de uso y practicidad, se opto por utilizar flask[^4], el cual facilita la creacion de la interfaz grafica, asi pues, el programa sera una aplicacion web.

### Resolucion de problema
lo primero a tratar seria como es que funcionaria la app por el lado del modelo, para esto se diseñaron los diagramas de flujo siguientes:

en el primero se ve la estrcutura bassica que seguira el programa dado un string de entrada, como se puede ver, primero de comprobara si el string es un ticket o no, si lo es, se llamara a `read()`, y si no lo es se llamara a `search()`, ademas se puede ver que read regresa una tupla de climas y search solo un clima.

en este se puede ver el funcionamiento de el metodo `read()`, que lo unico que hace es buscar en el dataset la fila que contiene el ticket y mandar a llamar a `search()`.

[^1]: https://openweathermap.org
[^2]: https://pandas.pydata.org
[^3]: https://pypi.org/project/requests/
[^4]: https://flask.palletsprojects.com/en/2.3.x/
