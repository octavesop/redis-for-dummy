import redis

try:
    conn = redis.StrictRedis(
        host='127.0.0.1',
        port=6379,
        password="aiground2017!"
    )
    print('connection success')
except Exception as ex:
    print('Error: ', ex)