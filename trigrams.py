def main(src, n):
	pass

	
def slice_book(src):
	"""will use text from src given, read it and split it at the spaces and return the list of words."""
	import io
	
	f = open(src, 'r')
	text = f.read()
	f.close()
	return text.split()
	
print(slice_book('drac_1-2.txt'))