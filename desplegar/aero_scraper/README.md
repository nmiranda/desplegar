Aero-scraper
============

Una aplicación de scraping de sitios web de aerolíneas, para encontrar los mejores precios.

Uso de la aplicación
--------------------

La vista principal (cuya url es el patrón vacío r'^$') debe recibir los siguientes parámetros GET:

* 'airline' : Código de la aerolínea (e.g. 'LAN')
* 'from_city' : Código del aeropuerto de origen (e.g. 'SCL')
* 'to_city' : Código del aeropuerto de destino (e.g. 'LIM')
* 'out_day' : Día de salida de vuelo deseado
* 'out_month' : Mes de salida de vuelo deseado
* 'out_year' : Año de salida de vuelo deseado
* 'in_day' : Día de llegada de vuelo deseado (opcional)
* 'in_month' : Mes de llegada de vuelo deseado (opcional)
* 'in_year' : Año de llegada de vuelo deseado (opcional)
* 'adults' : Número de adultos
* 'children' : Número de niños (opcional)
* 'infants' : Número de infantes (opcional)

Si el parámetro 'in_day' no está presente, se asumirá que el vuelo buscado es sólo de ida.

La aplicación, a su vez, retornará un JSON con los siguientes parámetros:

	{
		'out_price': Precio del mejor vuelo de salida
		'out_fly': Código del mejor vuelo de salida
		'out_airplane': Modelo de avión del mejor vuelo de salida
		'out_dep_time': Hora de despegue de avión del mejor vuelo de salida
		'out_arr_time': Hora de aterrizaje de avión del mejor vuelo de salida
		'out_length': Duración del mejor vuelo de salida
		'in_price': Precio del mejor vuelo de vuelta
		'in_fly': Código del mejor vuelo de vuelta
		'in_airplane': Modelo de avión del mejor vuelo de vuelta
		'in_dep_time': Hora de despegue de avión del mejor vuelo de vuelta
		'in_arr_time': Hora de aterrizaje de avión del mejor vuelo de vuelta
		'in_length': Duración del mejor vuelo de vuelta
		'url': La url de la cual se efectuó la consulta
	}

Si se buscó sólo vuelo de ida, el JSON de respuesta no tendrá los parámetros 'in_price', 'in_fly', 'in_airplane', 'in_dep_time', 'in_arr_time' e 'in_length'.
