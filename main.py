#print("hello world")

def countwords(book):
	words = book.split()
	return len(words)

def main():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
	print(f"{countwords(file_contents)} words found in the document.")

main()
