from datetime import datetime, timedelta
from typing import Union


class Time:
    """
    TODO: doc
    """

    def __init__(self, ut: Union[int, float]):
        # TODO: see if the format is good, if not, throw errors
        self.ut = ut
        self.dt_now = datetime.now()
        self.dt_local = datetime.fromtimestamp(ut)
        self.dt_utc = datetime.utcfromtimestamp(ut)
    
    @property
    def from_now(self) -> str:
        _diff = self.dt_local.timestamp() - self.dt_now.timestamp()

        ahead = True if _diff > 0 else False

        diff_td = timedelta(seconds=abs(_diff))
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

        return diff_str


x = Time(1552624334.4275699)
print(x.from_now)

print()