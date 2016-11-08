#!/usr/bin/python
import hashlib
import wordlist

length_word = 0
ch_alpha_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ch_alpha_l = 'abcdefghijklmnopqrstuvwxyz'
ch_numbers = '0123456789'
ch_symbol1 = '!@#$%^&*()_+-=,.'
ch_symbol2 = """`~[]\{}|;':"/<>?"""

# hex_dig = raw_input('SHA1: ')				
hex_dig = '54AE9735798588D2B67EB97DD90C542E485EAA59'							
								
generator = wordlist.Generator(ch_alpha_l + ch_alpha_u + ch_numbers + ch_symbol1)
for each in generator.generate(1, 20):	
	if(hex_dig == hashlib.sha1(each).hexdigest()):
		print(each)
		break



