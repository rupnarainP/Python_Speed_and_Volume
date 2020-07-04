import enum

class Urls(enum.Enum):
    Ookla = 'https://www.speedtest.net/insights/blog/tracking-covid-19-impact-global-internet-performance'\
            '/#/South%20Africa'
    IpBuffer = 'https://lp.buffer.com/state-of-remote-work-2020'

class FileName(enum.Enum):
    SpeedAndVolume = 'Internet Performance Tests.xlsx'
    Remote = 'State of Remote Work.xlsx'

class FileType(enum.Enum):
   Speed = 'Speeds'
   Remote = 'Remote'


