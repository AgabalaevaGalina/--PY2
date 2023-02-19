if __name__ == "__main__":
    # Write your solution here
    pass
class Book:

    def __init__(self, name:str, pages:int):
        """
        создание объекта базового класса Book
        :param name: название книги
        :param pages: кол-во страниц

        """
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f'Book(name={self.name!r}, pages={self.pages!r})'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f'error count of pages')
        else: raise AttributeError(f'error count of pages')
    def __str__(self):
        return f"Книга: {self.name} Автор: {self.author} Страниц:{self.pages}"