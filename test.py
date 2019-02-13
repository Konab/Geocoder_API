import time
from geocoder_51c import Geocoder_51c


# временное решение - словарик
true=True
false=False
null=None


def main():
	api = Geocoder_51c()
	# Test функция
	print('*** TEST ***')
	print(eval(api.test()))
	print(eval(api.test(address='Оренбург', house='61')))
	print()
	# Get_address_point функция
	print('*** Get_address_point ***')
	print(api.get_address_point('г Оренбург', 'Спартаковская', '61'))
	print(api.get_address_point('Оренбург', 'Спартаковская', '76'))
	print(api.get_address_point('Москва', 'Малый Ивановский', '11/6с1'))
	print(api.get_address_point('Москва', 'ул Большая Переяславская', '50'))
	print()
	# Get distance
	print('*** Get distance ***')
	print(eval(api.get_diapason(['51.7729901650272', '55.1257921703977'], ['51.7728556392302', '55.1253639126847'])))
	print(eval(api.get_diapason(['51.7729901650272', '55.1257921703977'], ['52.7728556392302', '56.1253639126847'])))
	print()
	# Get Closest point on roads
	print('*** Get Closest point on roads ***')
	print(eval(api.get_closest_point_on_road('Москва', 'ул Большая Переяславская', '50')))
	print(eval(api.get_closest_point_on_road('Москва', 'пер Малый Ивановский', '11/6с1')))
	print(eval(api.get_closest_point_on_road('Оренбург', 'ул Спартаковская', '61')))
	print()
	# Get correct point
	print('*** Get Closest point on roads ***')
	print(eval(api.get_correct_point('Москва', 'ул Большая Переяславская', '50', [55.786429, 37.640327])))
	print(eval(api.get_correct_point('Москва', 'пер Малый Ивановский', '11/6с1', [55.754063, 37.640616])))
	print(eval(api.get_correct_point('Оренбург', 'ул Спартаковская', '61', [51.773742, 55.125428])))
	print()
	# The new test
	print('*** TEST ***')
	print(eval(api.get_correct_point('Яранск', 'Карла Маркса', '181', [51.783742, 55.155428])))
	print(eval(api.get_closest_point_on_road('Яранск', 'Карла Маркса', '33')))
	print(eval(api.get_closest_point_on_road('Яранск', 'Карла Маркса', '29')))
	# Query with problem
	print('*** Query with problem ***')
	print(api.get_address_point('Яранск', 'Карла Маркса', '44'))
	print(eval(api.get_correct_point('Яранск', 'Карла Маркса', '26', [51.783742, 55.155428])))
	print(eval(api.get_correct_point('Яранск', 'Карла Маркса', '181', [51.783742, 55.155428])))
	print(eval(api.get_correct_point('Яранск', ' ул Карла Маркса', '44', [51.783742, 55.155428])))


if __name__ == '__main__':
	start_time = time.time()
	main()
	print('•'*40)
	print("--- %s seconds ---" % (time.time() - start_time))
