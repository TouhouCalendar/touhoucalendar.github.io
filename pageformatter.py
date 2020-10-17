from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(['html', 'xml'])
)

from touhoucalendar.touhou_calendar import DAYS, days_for, TouhouDay
from typing import NamedTuple, List
from urllib.parse import urlparse

class Day(NamedTuple):
    day: int
    touhoudays: List[TouhouDay]

class Month(NamedTuple):
    num: int
    name: str
    days: List[Day]

daykeys = sorted(DAYS.keys())
months = []
curmonth = None

MONTHNAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for key, touhoudays in sorted(DAYS.items()):
    month, day = key
    if curmonth is None or curmonth.num != month:
        curmonth = Month(month, MONTHNAMES[month-1], [])
        months.append(curmonth)

    curmonth.days.append(Day(day, touhoudays))

template = env.get_template("template.html")

print(template.render(months=months))


