import time

import schedule
from sharepoint_cleaner import main as cleaner
from sharepoint_uploader import main as uploader
from transfer_statistics import main as transfer_stats

schedule.every(1).hours.do(uploader)
schedule.every(1).hours.do(transfer_stats)
schedule.every().sunday.do(cleaner)
schedule.every().tuesday.do(cleaner)
schedule.every().thursday.do(cleaner)


while True:
    schedule.run_pending()
    time.sleep(10)
