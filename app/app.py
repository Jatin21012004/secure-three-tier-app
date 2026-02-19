from flask import Flask, jsonify
import redis 
import os 

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, socket_connect_timeout=2)

@app.route("/")
def hello ():
    try:
       r.incr("counter")
       count= r.get("counter").decode()
       return f"Hello devops! Page Visited {count} times"
    except  redis.exceptions.RedisError:
       return "Redis connection error", 500

@app.route("/health")
def health():
    try:
        r.ping()
        return jsonify(status="healthy"),200
    except redis.exceptions.RedisError:
        return jsonify(status="unhealthy", reason="redis unavailable"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
