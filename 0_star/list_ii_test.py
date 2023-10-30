from collections import Counter

def get_books():
    books = []
    while True:
        book = input()
        if book.lower() == 'end':
            break
        books.append(book)
    return books

def original_order(books):
    return {book: i + 1 for i, book in enumerate(books) if book not in books[:i]}

def main():
    book_list = get_books()
    sorted_books = sorted(set(book_list))
    book_counts = Counter(book_list)
    book_order = original_order(book_list)

    for book in sorted_books:
        index = book_order[book]
        count = book_counts[book]
        print(f'{book} {index} {count}')

if __name__ == "__main__":
    main()
