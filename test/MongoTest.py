import time
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

db = conn.default;

db.wechat.insert({"AccountId": 1212})

print(db.wechat.find_one())


def timing(func):
    def wrap(*args):
        time_begin = time.time();
        ret = func(args);
        time_end = time.time();
        print("function :%s time cost %d" % (func.__name__,(time_end-time_begin)*1000));
        return ret
    return wrap;


@timing
def hello(name):
    print("hello %s" % name)



hello("rocyuan")