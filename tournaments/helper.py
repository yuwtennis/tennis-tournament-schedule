from pytz import timezone
from datetime import datetime
import re


def parse_jpn_date(jpn_date_str: str, starts_at: str) -> datetime:

    match = re.match(r"(\d+)月(\d+)日.*", jpn_date_str)
    time = starts_at.split(':')
    jst = timezone('Asia/Tokyo')

    return jst.localize(match.group(1), match.group(2), 1, int(time[0]), int(time[1]))