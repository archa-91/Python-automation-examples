#!/usr/bin/python

import fb

#Refresh token before running script. Also allow uer friends access.
token = "EAACEdEose0cBAF9iyLZAZCZCyGevRbp0JTaR5ABikZBmm9IpG3ZCje5PNqWUmyD6GaU22muXUcPG8POZCgLbJNZA0BLd4rdRjUZBwnqKEzptCkZCFYgryroMin5Tz8lDM4qYKzZB12dCg9ybSsrlhm15CBCJL4NRnj1rfYWXl6O7VIC31A66rJF9DeS2YcLoJPjTQvuSTGtCkzEQZDZD"
facebook = fb.graph.api(token)
friends = facebook.get_object(cat = 'single', id = 'me', fields = ['friends'])
facebook.show_fields(friends)
for n in range(0,5):
	detail = facebook.get_object(cat = 'single',id = friends['friends']['data'][n]['id'],fields = ['gender']) 
	print friends['friends']['data'][n]['name']
	print detail['gender']
