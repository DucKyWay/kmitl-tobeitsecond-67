count = int(input())
bookshelf = []
for i in range(count):
    book_title = str(input())
    count_duplicate = bookshelf.count(book_title)
    if count_duplicate >= 2:
        pass
    elif count_duplicate == 0:
        bookshelf.append(book_title)
    else:
        index = bookshelf.index(book_title)
        bookshelf.insert(index, book_title)
print("ชั้นวางหนังสือ", bookshelf)