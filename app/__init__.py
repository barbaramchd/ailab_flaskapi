from flask import Flask, request
import redis
from rq import Queue, Connection

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)


from app import views
from app import tasks