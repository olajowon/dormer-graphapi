# Created by zhouwang on 2020/9/11.
from graphite_api.intervals import Interval, IntervalSet
import time
import hashlib
import taos
import threading
import configure


def lock(func):
    func.__lock__ = threading.Lock()

    def _w(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return _w


class TDengine:
    _instance = None

    @lock
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            connect = taos.connect(**configure.tdengine)
            TDengine._instance = connect
        return TDengine._instance


class Reader:
    def __init__(self, metric):
        self.metric = metric
        self.tdengine = TDengine()
        self.cursor = self.tdengine.cursor()

    def fetch(self, start_time, end_time):
        tab_name = 't_%s' % hashlib.md5(self.metric.encode(encoding='utf-8')).hexdigest()
        sql = '''SELECT LAST(value) FROM %s WHERE ts>=%d000 AND ts<%d999 INTERVAL (1m) FILL (NULL);
        ''' % (tab_name, start_time, end_time)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        series = [val if val else val for _, val in data]

        time_info = start_time // 60 * 60, end_time // 60 * 60, 60
        return time_info, series

    def get_intervals(self):
        return IntervalSet([Interval(0, int(time.time()))])