import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds023468.mlab.com:23468/moviedb

host = "ds023468.mlab.com"
port = 23468
db_name = "moviedb"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())