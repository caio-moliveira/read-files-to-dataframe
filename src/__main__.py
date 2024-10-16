import schedule 
import time
from lib.CsvSource import CsvSource


def check_for_new_files():

    csv_source = CsvSource()
    csv_source.check_for_new_files()


schedule.every(10).seconds.do(check_for_new_files)

while True:
    schedule.run_pending()
    time.sleep(1)

