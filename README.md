# Proyecto-Final-Pablo-Manzanares

![portada](https://as01.epimg.net/futbol/imagenes/2020/05/14/reportajes/1589479848_423331_1589716740_noticiareportajes_grande.jpg)



# Objetivo.

⚽ El objetivo del trabajo es el análisis de jóvenes promesas y jugadores veteranos con un valor actual inferior a 1M€. Para ello, se obtendrá la siguiente información: nombre, edad, equipo actual, nacionalidad, valor de mercado, valoración actual del jugador, valoración de futuro, valoración del equipo actual y valoraciones futbolísticas del mismo (ataque, defensa, regate, aceleración...).

❗ Además, es importante destacar que todas las **valoraciones se obtienen en rangos de 0 a 100** a partir de datos estadísticos de cada jugador. De este modo, dependiendo de los datos recogidos por su rendimiento en los partidos, se le otorga una puntuación de 0 a 100 en cada uno de los campos analizados.


🥅 La realización del proyecto constará de los siguientes puntos:

1️⃣ Realización de un web scraping con el objetivo de obtener la información más importante de las mayores promesas del mundo del fútbol con un valor inferior a 1M€.

2️⃣ Repetición del web scraping para jugadores más mayores, veteranos en el fútbol profesional, con un valor actual inferior a 1M€.

3️⃣ Una vez más, realización de un nuevo web scraping. Esta vez con jugadores jóvenes de distintos precios y características. De este modo, el objetivo, en este caso, es la obtención de un gran csv con el que poder realizar un modelo predictivo del precio de los jugadores dependiendo de sus características propias.

4️⃣ Realización de un modelo predictivo que permita obtener el precio de un jugador a partir de sus características y valoraciones.




# Obtención resultados.

✔ **Web scraping:** este método fue empleado para la obtención de las valoraciones y características de cada uno de los grupos de jugadores mencionados con anterioridad.

📈📊 Además, se estudiarán las características mediante gráficos de radar de manera individual y comparativa a modo de ejemplo, permitiendo un análisis más visual de los datos obtenidos. La elección de este tipo de gráfico es debido a que se trata de los más empleados en el mundo del fútbol.


✔ **Machine learning model** permite obtener un modelo predictivo con el que predecir el precio de un jugador dependiendo de sus características.

🥅🏃‍♂️ A partir del dataframe obtenido con una gran cantidad de jugadores de distintos precio y características, se realiza un modelo predictivo que permita la posterior tasación de un jugador.

En este caso, el procedimiento seguido ha sido:

1️⃣ Realización de una limpieza del dataframe original, previa exploración, para evitar outliers o nulos que puedan influir de manera negativa en los resultados del modelo. De esta forma, con la correcta gestión de estos datos es posible obtener un modelo más fiable.

2️⃣ División de los jugadores en clusters, lo que permite analizar de manera independiente cada uno de ellos para obtener el precio correcto dependiendo de sus características. Así, obtenemos tres grandes grupos de jugadores: atacantes, defensas y porteros. 

3️⃣ Realización de un pipeline que permita determinar el mejor modelo predictivo para cada cluster de jugadores.

4️⃣ Aplicación del modelo más apropiado a cada uno de los cluster de jugadores, lo que permite obtener una aproximación del precio, en euros, del jugador.


✔ **Streamlit** permite la presentación del producto final en un dashboard.




# Estructura del proyecto.

1️⃣ **notebook:** contiene los jupyter de trabajo. Se ha divido a su vez en carpetas.

*jovenespromesas:* web scraping y obtención del dataframe con las jóvenes promesas.

*modeloprecio:* modelo predictivo del precio de los jugadores.

*proyeccionprecio:* dataframe con gran cantidad de jugadores jóvenes que permita el correcto fiteo del modelo predictivo.
    
*veteranos:* web scraping y obtención del dataframe con jugadores veteranos y valor inferior a 1M€. 

*visualizacion:* gráficos que permiten un análisis visual de las características de los jugadores.

2️⃣ **images:** imágenes de las gráficas obtenidas y otras empleadas en las presentaciones.

3️⃣ **data:** distintos csv obtenidos en el proyecto. En etse caso, también se dividen por carpetas.

*precio:* csv relativo a la obtención del modelo predictivo.

*promesas:* csv con cada una de las características de las jóvenes promesas obtenidas.

*veteranos:* csv con cada una de las características de los jugadores veteranos obtenidos.

4️⃣ **Streamlit:** presentación en un dashboard del producto final obtenido mediante la realización del proyecto.

❗ En este caso, es importante destacar la utilización de la librería pickle, la cual nos permite guardar los modelos fiteados para ofrecer al usuario la posibilidad de añadir características de un jugador y, en base a ellas, estimar un precio del jugador. En definitiva, permite al usuario interaccionar con el dashboard para obtener resultados a partir de sus propios datos.

⚽ De este modo, se guardan los modelos ajustados para cada uno de los clusters, de modo que al añadir el usuario datos de un jugador, en primer lugar lo etiquetará en un cluster y, posteriormente, empleando el modelo específico para ese cluster, determinará su precio.



# Librerías.

[pandas] (https://pandas.pydata.org/)

[numpy] (https://numpy.org/)

[regex] (https://docs.python.org/3/library/re.html)

[request] (https://docs.python-requests.org/en/latest/)

[bs4] (https://pypi.org/project/beautifulsoup4/)

[pickle] (https://docs.python.org/3/library/pickle.html)

[sklearn] (https://scikit-learn.org/stable/)

[scipy] (https://scipy.org/)

[matplotlib] (https://matplotlib.org/)

[seaborn] (https://seaborn.pydata.org/)

[statsmodel] (https://www.statsmodels.org/stable/index.html)

[plotly] (https://plotly.com/python/)




