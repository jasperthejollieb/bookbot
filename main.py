from stats import no_words, no_chars, newd

def get_book_text(path):
	with open(path) as f:
		return f.read()

def sort_newd(newd):
	return newd["count"]



def main():
#	print(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt"))
	no_words(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt"))
#	print(no_chars(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt")))
	b = no_chars(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt"))
	c = newd(b)
	c.sort(reverse=True, key=sort_newd)
	print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
	print(f"Found {no_words(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt"))} total words\n--------- Character Count -------")
	for dict in c:
		print(f"{dict['char']}: {dict['count']}")
	print("============= END ===============")
main()
