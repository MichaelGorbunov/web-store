from django.core.management import call_command
from django.core.management.base import BaseCommand

# from students.models import Student, Group

# class Command(BaseCommand):
#     help = 'Add test students to the database'
#
#     def handle(self, *args, **kwargs):
#         group, _ = Group.objects.get_or_create(name='Группа 1')
#
#         students = [
#             {'first_name': 'Иван', 'last_name': 'Иванов', 'year': Student.FIRST_YEAR, 'group': group},
#             {'first_name': 'Петр', 'last_name': 'Петров', 'year': Student.SECOND_YEAR, 'group': group},
#             {'first_name': 'Сергей', 'last_name': 'Сергеев', 'year': Student.THIRD_YEAR, 'group': group},
#         ]
#
#         for student_data in students:
#             student, created = Student.objects.get_or_create(**student_data)
#             if created:
#                 self.stdout.write(self.style.SUCCESS(f'Successfully added student: {student.first_name} {student.last_name}'))
#             else:
#                 self.stdout.write(self.style.WARNING(f'Student already exists: {student.first_name} {student.last_name}'))




class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        call_command("loaddata", "students_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
