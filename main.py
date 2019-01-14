import argparse
import pytz
from datetime import datetime, timedelta

from lib.scrap import TimezoneScrapper


def format(dt: datetime) -> str:
    return dt.strftime('%a, %b %d, %Y %I:%M%p')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ut', type=float)
    parser.add_argument('--city', '-c', type=str, required=False)
    parser.add_argument('--diff', '-d', action='store_true')
    args = parser.parse_args()

    # TODO: error handling, number of digits should be either 10 (s) till 2033 or 13 (ms)

    # TODO: move city below diff, add placehoulder to show that the scrapper is running, and add a wink or sth face to show the result

    ut = args.ut
    
    dt_local = datetime.fromtimestamp(ut)
    print(f'Local: {format(dt_local)}')

    dt_utc = datetime.utcfromtimestamp(ut)
    print(f'GMT  : {format(dt_utc)}')
    

    if args.city:
        ts = TimezoneScrapper(args.city)
        if ts.timezone:
            tz_sign = ts.timezone[0]
            tz_diff = int(ts.timezone[1:])
            if tz_sign == '-':
                dt_city_ut = dt_utc.timestamp() - tz_diff * 3600
            elif tz_sign == '+':
                dt_city_ut = dt_utc.timestamp() + tz_diff * 3600

            dt_city = datetime.fromtimestamp(dt_city_ut)
            print(f'{args.city}: {format(dt_city)}')
        else:
            print(u'\U0001F925',
                  ' emmm... I cannot find your city on popular search engines!')

    if args.diff:
        dt_now = datetime.now()
        
        diff = dt_local.timestamp() - dt_now.timestamp()

        ahead = True if diff > 0 else False

        diff_td = timedelta(seconds=abs(diff))
        diff_d = diff_td.days
        diff_s = diff_td.seconds

        diff_h = diff_s // 3600
        diff_s -= diff_h * 3600
        diff_m = diff_s // 60
        diff_s -= diff_m * 60

        diff_str = 'Given time is '
        if diff_d != 0:
            diff_str += f'{diff_d} days, '
        if diff_h != 0:
            diff_str += f'{diff_h} hrs, '
        if diff_m != 0:
            diff_str += f'{diff_m} mins, '
        diff_str += f'{diff_s} secs '
        diff_str += 'ahead' if ahead else 'ago'
        
        print(diff_str)


if __name__ == '__main__':
     main()
