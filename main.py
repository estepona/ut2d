import argparse
import pytz
from datetime import datetime


def format(dt: datetime) -> str:
    return dt.strftime('%a, %b %d, %Y %I:%M%p')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ut', type=float)
    parser.add_argument('--city', type=str, required=False)
    parser.add_argument('--diff', '-d', action='store_true')
    args = parser.parse_args()

    # TODO: error handling, number of digits should be either 10 (s) till 2033 or 13 (ms)

    # TODO: add a relative field

    # TODO: if search by city, just use the web, add emoji. get time here: https://www.timeanddate.com/

    ut = args.ut
    
    dt_local = datetime.fromtimestamp(ut)
    print(f'Local: {format(dt_local)}')

    dt_utc = datetime.utcfromtimestamp(ut)
    print(f'GMT  : {format(dt_utc)}')
    
    if args.diff:
        dt_now = datetime.now()
        print('now', dt_now)

        diff = dt_now - dt_local
        days = diff.days
        secs = diff.seconds

        # TODO: calculation with timedelta is wrong, use timestamp instead
        
        # diff_detail = diff.split(',')
        # if len(diff_detail) == 2:
        #     print(diff_detail)
        print(diff.days)
        print(diff.seconds)
        
        print('diff', diff)


if __name__ == '__main__':
     main()