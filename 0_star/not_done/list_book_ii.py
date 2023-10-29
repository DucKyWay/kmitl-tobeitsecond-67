from collections import Counter

book_list = []
while True:
    book = input()
    if book.lower() == "end":
        break
    book_list.append(book)
    
original_order = {book: i+1 for i, book in enumerate(book_list)}

book_list_sorted = sorted(book_list)
book_count = Counter(book_list)

for book in book_list_sorted:
    if book in original_order:
        first_index = original_order[book]
        count = book_count[book]
        print(book, first_index, count)
        del original_order[book]