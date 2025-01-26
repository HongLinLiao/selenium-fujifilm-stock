import time
import schedule
from check_stock import check_product_stock

print("🚀 Start checking stock...")

# schedule.every(3).seconds.do(check_product_stock)
schedule.every(1).minutes.do(check_product_stock)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stop")