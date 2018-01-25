def main(src, n):
	list = slice_book(src)
	dict = book_dict(list)
	print(dict)

	
def slice_book(src):
	"""will use text from src given, read it and split it at the spaces and return the list of words."""
	import io
	
	f = open(src, 'r')
	text = f.read()
	f.close()
	text = text.split()
	
	return text
	
list = slice_book('drac_1-2.txt')

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
	

main('drac_1-2.txt', 0)
	
	

#print(slice_book('drac_1-2.txt'))
#print(book_dict(list))