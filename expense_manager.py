from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime
import pytz
from urllib.parse import unquote

app = Flask(__name__)
api = Api(app)

class WorldTime(Resource):
  def get(self, timezone):
    timezone = unquote(timezone)
    if timezone in pytz.all_timezones:
      tz = pytz.timezone(timezone)
      tz_now = datetime.now(tz)
      fmt = '%Y-%m-%d %H:%M:%S %Z%z'
      return {'WorldTime': str(tz_now.strftime(fmt))}
    else:
      return {'WorldTime': 'error'}
  

api.add_resource(WorldTime, '/WorldTime/<string:timezone>')

if __name__ == '__main__':
  app.run(debug=True)