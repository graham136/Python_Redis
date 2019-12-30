import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379)

print("Setting Key1 with a value KeyValue1")
r.set('Key1','KeyValue1')
print("Retrieving Key1 with a value KeyValue1")
value = r.get('Key1')
print(value)
