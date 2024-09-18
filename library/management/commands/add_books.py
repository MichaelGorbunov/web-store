from django.core.management.base import BaseCommand

from library.models import Author, Book


class Command(BaseCommand):
    help = "Add test books to the database"

    def handle(self, *args, **kwargs):
        author, _ = Author.objects.get_or_create(
            first_name="Антон", last_name="Чехов", birth_date="1860-01-29"
        )
        author1, _ = Author.objects.get_or_create(
            first_name="Лев", last_name="Толстой", birth_date="1828-09-09"
        )
        author2, _ = Author.objects.get_or_create(
            first_name="Федор", last_name="Достоевский", birth_date="1821-11-11"
        )

        books = [
            {
                "title": "Вишневый сад",
                "publication_date": "1904-01-01",
                "author": author,
            },
            {"title": "Три сестры", "publication_date": "1901-01-01", "author": author},
            {
                "title": "Война и мир",
                "publication_date": "1869-01-01",
                "author": author1,
            },
            {
                "title": "Анна Каренина",
                "publication_date": "1877-01-01",
                "author": author1,
            },
            {
                "title": "Преступление и наказание",
                "publication_date": "1866-01-01",
                "author": author2,
            },
        ]

        for book_data in books:
            book, created = Book.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added book: {book.title}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Book already exists: {book.title}")
                )
