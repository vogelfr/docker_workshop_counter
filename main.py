import redis
import os
import time
from flask import Flask
app = Flask(__name__)

redis_location = os.environ["REDIS_LOCATION"] or "redis"
r = redis.StrictRedis(host=redis_location, port=6379, db=0)


@app.route("/")
def index():
	r.rpush("visits", time.time())
	count = r.llen("visits")
	if count == 1:
		return "You have accessed this website {count} time".format(count=count)
	else:
		return "You have accessed this website {count} times".format(count=count)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)


