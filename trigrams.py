
def main(src, n):
	import random
	word_list = slice_book(src)
	dict = book_dict(word_list)
	
	dict_keys = random.choice(list(dict.keys()))
	value = dict.get(dict_keys)
	random_value = random.choice(value)
	paragraph = dict_keys.split()
	
	
	paragraph.append(random_value)
	
	for i in range(1, n):
		paragraph.append(random.choice(dict[paragraph[i] + ' ' + paragraph[i+1]]))
		
	par_string = ' '.join(paragraph)
	
	#for i in range(n):
		 
		
	
	#if len(paragraph) < n:
		
	#with that key add it's value (word) to the paragraph
	#while len(paragraph) < n:
		
	
	
	
	
	#print(dict_keys)
	print(paragraph)
	print(par_string)
	

	
def slice_book(src):
	"""will use text from src given, read it and split it at the spaces and return the list of words."""
	import io
	
	f = open(src, 'r', encoding='utf8')
	text = f.read()
	f.close()
	text = text.split()
	strip_text = [ ]
	for word in text:
		strip_text.append(word.strip('.!,_;?"'))
	
	return strip_text
	
#lists = slice_book('sawyer.txt')

def book_dict(list):
	"""takes a list of strings ['a','b','c','d']
	and creates dictionary of trigrams as follows:
	{'a b': ['c'], 'b c': [d]}
	"""
	dict = {'the the': ['the']}
	
	for i in range(0, len(list)):
		if i < len(list) - 2:
			if list[i] + " " + list[ i + 1] not in dict:
				dict[ list[i] + " " + list[ i + 1] ] = [list[i+2]]
			else:
				dict[ list[i] + " " + list[ i + 1] ] = dict[ list[i] + " " + list[ i + 1] ] + [list[ i + 2 ]]
			
				
	return dict


	
main('sawyer.txt', 10)
