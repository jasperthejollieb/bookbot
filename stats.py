def no_words(text):
       # print(f"{len(text.split())} words found in the document")
	return len(text.split())
def no_chars(text):
	a = {}
	for char in text:
		if char.lower() in a:
			a[char.lower()] += 1
		else: a[char.lower()] = 1
	return a

def newd(d):
	b = []
	for char in d:
		if char.isalpha():	
			b.append({"char": char, "count": d[char]})
	return b
# def sortf(d):
#	return d[char][]
