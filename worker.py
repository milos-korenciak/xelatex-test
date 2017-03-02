import os
from redis import Redis
import time
import datetime
import random
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
redis = Redis()
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

i = random.random()
while 1:
    print("Hello worker {} on {}!".format(i, datetime.datetime.now()))
    time.sleep(60)
