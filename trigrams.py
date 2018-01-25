def main(src, n):
	pass

	
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
	"""takes a list of strings and creates dictionary with two words as key, third work as value"""
	dict = {'the the': ['the']}
	
	for i in range(0, len(list)):
		if i < len(list) - 2:
			if list[i] + " " + list[ i + 1] not in dict:
				dict[ list[i] + " " + list[ i + 1] ] = [list[i+2]]
			else:
				dict[ list[i] + " " + list[ i + 1] ] = dict[ list[i] + " " + list[ i + 1] ] + [list[ i + 2 ]]
			
				
	return dict
	
	
	

print(slice_book('drac_1-2.txt'))
print(book_dict(list))