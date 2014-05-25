# -*- coding: utf-8 -*-

import urllib2
import re
import string
from bs4 import BeautifulSoup

cities = {
	'SCL': 'Santiago, Chile',
	'LIM': 'Lima, Perú',
	'CCP': 'Concepción, Chile',
}

def getRequestString(airline, from_city, to_city, outward_date, adults, return_date=None, children=0, infants=0):
	if airline == 'LAN':
		if return_date is None:
			ida_vuelta = 'ida'
			return_date = ('','','')
		else:
			ida_vuelta = 'ida_vuelta'
		format_string = 'http://booking.lan.com/cgi-bin/compra/paso2.cgi?fecha1_dia={:02d}&fecha1_anomes={}-{:02d}&fecha2_dia={:02d}&fecha2_anomes={}-{:02d}&otras_ciudades=&num_segmentos_interfaz=2&tipo_paso1=caja&rand_check=169.26443761278387&from_city2={}&to_city2={}&auAvailability=1&ida_vuelta={}&from_city1={}&to_city1={}&flex=1&cabina=Y&nadults={}&nchildren={}&ninfants={}'
		request_string = format_string.format(
			outward_date[0],
			outward_date[2],
			outward_date[1],
			return_date[0],
			return_date[2],
			return_date[1],
			to_city,
			from_city,
			ida_vuelta,
			from_city,
			to_city,
			adults,
			children,
			infants,
			)
		return request_string

def getBestPrices(airline, from_city, to_city, outward_date, adults, return_date=None, children=0, infants=0):

	request_string = getRequestString(airline=airline, from_city=from_city, to_city=to_city, outward_date=outward_date, return_date=return_date, adults=adults, children=children, infants=infants)
	request = urllib2.Request(request_string)
	request.add_header('Cookie', 'pcom=espanol%2Fcl')
	responseData = urllib2.urlopen(request).read()

	soup = BeautifulSoup(responseData)

	out_flies = soup.find_all('td', attrs={'onclick':re.compile('vueloida')})

	out_min_node =  min(out_flies, key=(lambda qwe: float(qwe.get_text().strip(string.whitespace)[qwe.get_text().strip(string.whitespace).index('$')+1:].replace(',',''))))

	out_min_node_fly = out_min_node.parent.td.span.strong.get_text().strip(string.whitespace)

	out_min_node_airplane = out_min_node.parent.td.span.next_sibling.span.get_text().strip(string.whitespace)

	out_min_node_dep_time = out_min_node.parent.td.next_sibling.next_sibling.span.get_text().strip(string.whitespace)

	out_min_node_arr_time = out_min_node.parent.td.next_sibling.next_sibling.next_sibling.next_sibling.span.get_text().strip(string.whitespace)
	out_min_node_length = out_min_node.parent.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip(string.whitespace)

	if return_date == None:
		return {
			'out_price': out_min_node.get_text().strip(string.whitespace),
			'out_fly': out_min_node_fly,
			'out_airplane': out_min_node_airplane,
			'out_dep_time': out_min_node_dep_time,
			'out_arr_time': out_min_node_arr_time,
			'out_length': out_min_node_length,
			'url': request_string
		}

	else:
		in_flies = soup.find_all('td', attrs={'onclick':re.compile('vuelovuelta')})

		in_min_node =  min(in_flies, key=(lambda qwe: float(qwe.get_text().strip(string.whitespace)[qwe.get_text().strip(string.whitespace).index('$')+1:].replace(',',''))))

		in_min_node_fly = in_min_node.parent.td.span.strong.get_text().strip(string.whitespace)

		in_min_node_airplane = in_min_node.parent.td.span.next_sibling.span.get_text().strip(string.whitespace)

		in_min_node_dep_time = in_min_node.parent.td.next_sibling.next_sibling.span.get_text().strip(string.whitespace)

		in_min_node_arr_time = in_min_node.parent.td.next_sibling.next_sibling.next_sibling.next_sibling.span.get_text().strip(string.whitespace)
		in_min_node_length = in_min_node.parent.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text().strip(string.whitespace)

		return {
			'out_price': out_min_node.get_text().strip(string.whitespace),
			'out_fly': out_min_node_fly,
			'out_airplane': out_min_node_airplane,
			'out_dep_time': out_min_node_dep_time,
			'out_arr_time': out_min_node_arr_time,
			'out_length': out_min_node_length,
			'in_price': in_min_node.get_text().strip(string.whitespace),
			'in_fly': in_min_node_fly,
			'in_airplane': in_min_node_airplane,
			'in_dep_time': in_min_node_dep_time,
			'in_arr_time': in_min_node_arr_time,
			'in_length': in_min_node_length,
			'url': request_string
		}


def main():

	best_prices = getBestPrices(airline='LAN', from_city='SCL', to_city='LIM', outward_date=(1, 6, 2014), return_date=(1, 6, 2014), adults=1)

	print best_prices

	#request = urllib2.Request('http://booking.lan.com/cgi-bin/compra/paso2.cgi?fecha1_dia=20&fecha1_anomes=2014-05&fecha2_dia=20&fecha2_anomes=2014-05&otras_ciudades=&num_segmentos_interfaz=2&tipo_paso1=caja&rand_check=169.26443761278387&from_city2=LIM&to_city2=SCL&auAvailability=1&ida_vuelta=ida_vuelta&vuelos_origen=Santiago%20de%20Chile,%20Chile%20%28SCL%29&from_city1=SCL&vuelos_destino=Lima,%20Per%FA%20%28LIM%29&to_city1=LIM&flex=1&vuelos_fecha_salida=20/MAY/2014&vuelos_fecha_salida_ddmmaaaa=20/05/2014&vuelos_fecha_regreso=20/MAY/2014&vuelos_fecha_regreso_ddmmaaaa=20/05/2014&cabina=Y&nadults=1&nchildren=0&ninfants=0')
	#request = urllib2.Request(request_string)
	#request.add_header('Cookie', 'pcom=espanol%2Fcl')
	#responseData = urllib2.urlopen(request)

	#print responseData.read()


		


if __name__ == '__main__':
	main()