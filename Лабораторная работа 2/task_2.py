BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть целым числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги не является строкой")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books
        if books is None:
            self.books = []

    def get_next_book_id(self):
        if self.books == []:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, books_id_: int):
        if not isinstance(books_id_, int):
            raise TypeError("id книги должен быть типа int")
        book_index = None
        list_id = []
        for i in range(len(self.books)):
            list_id.append(self.books[i].id_)
        for index, current_id in enumerate(list_id):
            if current_id == books_id_:
                book_index = index
        if book_index is None:
            raise ValueError("Книги с запрашиваемым id не существует")
        return book_index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
