from datetime import date


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library:\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Open hours: {self.open_hours}\n"
            f"  Phone: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: date,
        birth_date: date,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"  Employee: {self.first_name} {self.last_name}\n"
            f"  Hire date: {self.hire_date}\n"
            f"  Birth date: {self.birth_date}\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Phone: {self.phone}"
        )


class Student:
    # Tworze klase studenci.
    def __init__(self, first_name: str, last_name: str, student_id: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.phone = phone

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (ID: {self.student_id}, phone: {self.phone})"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: date,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book:\n"
            f"  Author: {self.author_name} {self.author_surname}\n"
            f"  Publication date: {self.publication_date}\n"
            f"  Pages: {self.number_of_pages}\n"
            f"  Available in:\n"
            f"{self.library}"
        )


class Order:
    def __init__(self, employee: Employee, student: Student, books: list[Book], order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(
            [
                f"  - {b.author_name} {b.author_surname}, {b.publication_date}, {b.number_of_pages} pages "
                f"(library: {b.library.city}, {b.library.street})"
                for b in self.books
            ]
        )

        return (
            f"ORDER (date: {self.order_date})\n"
            f"{self.student}\n"
            f"Handled by:\n{self.employee}\n"
            f"Books:\n{books_str}"
        )


# Tworzenie obiektów

# 2 biblioteki
lib1 = Library("Warszawa", "ul. Mickiewicza 10", "01-517", "Mon-Fri 08:00-18:00", "+48 22 111 22 33")
lib2 = Library("Kraków", "ul. Długa 5", "31-146", "Mon-Sat 09:00-17:00", "+48 12 444 55 66")

# 3 pracowników
emp1 = Employee("Anna", "Kowalska", date(2020, 3, 1), date(1993, 7, 12), "Warszawa", "ul. Polna 2", "00-635", "500-111-222")
emp2 = Employee("Piotr", "Nowak", date(2018, 9, 15), date(1988, 2, 3), "Warszawa", "ul. Marszałkowska 40", "00-545", "500-333-444")
emp3 = Employee("Kasia", "Wiśniewska", date(2022, 1, 10), date(1998, 11, 20), "Kraków", "ul. Karmelicka 12", "31-128", "500-555-666")

# 3 studentów
st1 = Student("Jan", "Lis", "S12345", "600-101-202")
st2 = Student("Ola", "Maj", "S54321", "600-303-404")
st3 = Student("Marek", "Zając", "S77777", "600-505-606")

# 5 książek
b1 = Book(lib1, date(2010, 5, 10), "Andrzej", "Sapkowski", 320)
b2 = Book(lib1, date(1997, 6, 26), "J.K.", "Rowling", 223)
b3 = Book(lib2, date(1866, 1, 1), "Fiodor", "Dostojewski", 671)
b4 = Book(lib2, date(1949, 6, 8), "George", "Orwell", 328)
b5 = Book(lib1, date(1937, 9, 21), "J.R.R.", "Tolkien", 310)

# 2 zamówienia
order1 = Order(emp1, st1, [b1, b2, b5], date(2025, 12, 10))
order2 = Order(emp3, st2, [b3, b4], date(2025, 12, 12))

# Wyświetlenie obu zamówień
print(order1)
print("\n" + "=" * 60 + "\n")
print(order2)