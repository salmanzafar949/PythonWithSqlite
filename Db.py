import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from  matplotlib import style
#define the connection

conn = sqlite3.connect('demo.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def insert_data():
    c.execute("INSERT INTO stuff VALUES(123456,'2017-12-23', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%n-%d %H:%M:%S'))
    keyword = 'php'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuff (unix, datestamp, keyword, value) VALUES(?,?,?,?)",(unix, date, keyword, value))
    conn.commit()
    #c.close()

def display_data():
    c.execute("SELECT * FROM stuff")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute("SELECT unix, value FROM stuff")
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
        plt.plot_date(dates, values, '-')
        plt.show()

graph_data()
#display_data()
#
#create_table()
# insert_data()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

c.close()
conn.close()