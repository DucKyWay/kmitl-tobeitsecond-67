from collections import Counter

book_list = []

while True:
    book = input()
    if book.lower() == "end":
        break
    book_list.append(book)

chk_book.sort()
book_count = Counter(book_list)
chk_book = list(book_count.keys())

for i, book in enumerate(chk_book, start=1):
    count = book_count[book]
    print(book, i, count)