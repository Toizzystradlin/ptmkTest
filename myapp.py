import fire
import mysql.connector
import random
import string
import time
from random import randrange
from datetime import timedelta
from datetime import datetime

db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='12345',
        port='3306',
        database='ptmk'
    )
cursor = db.cursor(True)

class App(object):

    def create_person(self, fio, birthday, sex):
        cursor.execute("INSERT INTO people (fio, birthday, sex) VALUES (%s, %s, %s)", [fio, birthday, sex])
        db.commit()
        return print('в базе создана запись: ' + str(fio) + '-' + str(birthday) + '- пол: ' + str(sex))

    def uniqs(self):
        cursor.execute("SELECT DISTINCT CONCAT(fio, birthday), sex FROM people ORDER BY fio")
        data = cursor.fetchall()
        return data

    def random_n(self, lenght=10, First_letter=None):

        def random_date(start=datetime.strptime('1/1/1900 1:00 PM', '%m/%d/%Y %I:%M %p'), end=datetime.strptime('1/1/2021 1:00 AM', '%m/%d/%Y %I:%M %p')):
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = randrange(int_delta)
            return start + timedelta(seconds=random_second)

        letters = string.ascii_lowercase
        Big_letter = string.ascii_uppercase
        if First_letter != None:
            Big_letter = First_letter

        for i in range(lenght):
            rand_string = random.choice(Big_letter)
            for i in range(10):
                rand_string = rand_string + '' + str(random.choice(letters))
            m_or_f = 'mf'
            cursor.execute("INSERT INTO people (fio, birthday, sex) VALUES (%s, %s, %s)", [rand_string, random_date(), random.choice(m_or_f)])
            db.commit()
            #print(random_date())
            #print(random.choice(m_or_f))

        return print('Создано ' + str(lenght) + ' строк')

    def select(self, sex, fio_starts_with):
        start = time.time()
        cursor.execute("SELECT fio, birthday, sex FROM people WHERE sex = %s AND LEFT(fio, 1) = %s", [sex, fio_starts_with])
        #cursor.execute("SELECT * FROM people WHERE sex = %s", [sex])
        data = cursor.fetchall()
        end = time.time()

        return print(data, 'Время исполнения: ' + str(end - start))

if __name__ == '__main__':
    fire.Fire(App)