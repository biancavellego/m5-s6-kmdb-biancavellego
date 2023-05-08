from django.core.management.base import BaseCommand, CommandParser, CommandError
from django.utils.crypto import get_random_string
from users.models import User

# Creating custom commands:
# OBS: python manage.py createsuperuser is a defaut CLI.

# On terminal: python manage.py create_admin
class Command(BaseCommand):
    help = "Creates an admin user."

    def add_arguments(self, parser: CommandParser) -> None:
        # Non-optional arguments:
        # parser.add_argument(
        #     "is_superuser", type=bool, help="Define if user will be admin or not."
        # )

        # Optional arguments:
        # OBS: they have a "--" symbol to distinguish them.
        # All flags with just one "-", are abbreviations.
        parser.add_argument("-u", "--username", type=str, help="Define admin username.")
        parser.add_argument("-p", "--password", type=str, help="Define admin password.")
        parser.add_argument("-e", "--email", type=str, help="Define admin email.")

    def handle(self, *args: tuple, **options: dict) -> str | None:
        username = options.get("username")
        password = options.get("password")
        email = options.get("email")

        if username:
            username = username
        else:
            username = "admin"

        if password:
            password = password
        else:
            password = "admin1234"

        if email:
            email = email
        else:
            email = username + "@example.com"

        # Consulting table "users" (User) to check if a certain data already exists:
        usernameAlreadyExists = User.objects.filter(username=username)
        emailAlreadyExists = User.objects.filter(email=email)

        if usernameAlreadyExists:
            raise CommandError(f"Username `{username}` already taken.")
        if emailAlreadyExists:
            raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )

        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!")
        )
