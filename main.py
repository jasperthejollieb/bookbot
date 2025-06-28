import sys
from stats import no_words, no_chars, newd

def get_book_text(path):
	with open(path) as f:
		return f.read()

def sort_newd(newd):
	return newd["count"]



def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
#		print(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt"))
		arg2 = sys.argv[1]
		no_words(get_book_text(arg2))
#		print(no_chars(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt")))
		b = no_chars(get_book_text(arg2))
		c = newd(b)
		c.sort(reverse=True, key=sort_newd)
		print(f"============ BOOKBOT ============\nAnalyzing book found at {arg2}...\n----------- Word Count ----------")
		print(f"Found {no_words(get_book_text("/home/fors/bookbot/bookbot/books/frankenstein.txt"))} total words\n--------- Character Count -------")
		for dict in c:
			print(f"{dict['char']}: {dict['count']}")
		print("============= END ===============")
main()
