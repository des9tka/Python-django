from time import sleep

from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.dummy.base import DatabaseWrapper

connection: DatabaseWrapper = connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        db_con = False

        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except (OperationalError,):
                self.stdout.write('DataBase is unavailable. Reconnect in 1 second...')
                sleep(1)
        self.stdout.write("DataBase is available!")
