class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f'error count of pages')
        else: raise AttributeError(f'error count of pages')


      #  self.name = name
       # self.author = author
        #self.pages = pages

    def __str__(self):
        return f"Книга: {self.name} Автор: {self.author} Страниц:{self.pages}"

     #   return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise AttributeError(f'error time of duration')
        else:
            raise AttributeError(f'error type')
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. продолжительность:{self.duration}"

Book1 = Book("ThePictureOfDorianGray", "OscarWilde")
print(Book1)
Book2 = PaperBook("ThePictureOfDorianGrayPaper", "OscarWilde", 230)
print(Book2)
Book3 = AudioBook("ThePictureOfDorianGrayAu", "OscarWilde", 180)
print(Book3)

       


