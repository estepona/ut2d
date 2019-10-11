import sys
import time

from ut2d.lib import EMOJI, parse_args, throw_msg, TimezoneScrapper, Time


def main():
  args = parse_args(sys.argv[1:])

  if args.ut_or_now == 'now':
    ut = time.time()
  else:
    if Time.is_valid(args.ut_or_now):
      ut = args.ut_or_now
    else:
      throw_msg(1, 'arg_invalid', True)

  dt = Time(ut)

  print(f'Unix Timestamp: {ut}')
  print(f'Local: {Time.fmt(dt.local)}')
  print(f'GMT  : {Time.fmt(dt.utc)}')

  if args.diff:
    print(dt.from_now)

  if args.timezone:
    if args.timezone[:3].upper() not in ['GMT', 'UTC']:
      throw_msg(1, 'tz_fmt_invalid', True)
    else:
      dt_tz = dt.in_timezone(args.timezone)
      print(f'{EMOJI["smiling_face_with_sunglasses"]}  The given time in {args.timezone} is: {Time.fmt(dt_tz)}.')

  if args.city:
    throw_msg(0, 'search_tz_begin')

    dt_city = dt.in_city(args.city)
    print(
      f'{EMOJI["smiling_face_with_sunglasses"]}  I suppose the given time in {args.city} is: {Time.fmt(dt_city)}.'
      ' I have 88% confidence with this result from search engines!'
    )


if __name__ == '__main__':
  main()
