#print("hello world")

def countwords(book_split):
	words = book_split.split()
	return len(words)

def lettercount(book):
	letter_dict = {}
	# book_string = book.replace(' ', '')
	for letter in book:
		lowered = letter.lower()
		if lowered in letter_dict:
			letter_dict[lowered] += 1
		else:
			letter_dict[lowered] = 1
	return sort_list(letter_dict)

def sort_list(sorted_list):
	final_sort = []
	for sorted_letter in sorted_list:
		final_sort.append({"char": sorted_letter, "num": sorted_list[sorted_letter]})
	return final_sort


def main():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
	print(f"{countwords(file_contents)} words found in the document.")
	print("Letter count:")
	returned_list = lettercount(file_contents)
	for each_letter in returned_list:
		if not each_letter["char"].isalpha():
			continue
		else:
			print(f"The letter {each_letter["char"]} was found {each_letter["num"]} times")


main()
