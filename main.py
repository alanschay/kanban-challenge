import os,json,uuid,sys
from datetime import datetime
from flask import Flask
from flask import request,session,redirect,url_for,escape,send_from_directory,render_template
from flask_cors import CORS


app = Flask(__name__,static_url_path='')

cors = CORS(app)

sort_keys = True
indent = 4

def cypher(data):
    encoded = ""
    for character in data:
        encoded += chr(((ord(character) + Shift) % 128)) # The spec requires that characters overflow to 0, which may cause undesired behavior from control codes.
    return encoded
    
def decypher(data):
    decoded = ""
    for character in data:
        decoded += chr((((ord(character) - Shift) % 128) + 128) % 128) # Slightly screwy, but the logic is to shift, mod down to some number between [-127,127], add 128 to escape negatives, and mod again for [0,127]
    return decoded
    
def save(data):
    f = open(Loads,'w')
    try:
        f.write(cypher(json.dumps(data,sort_keys=sort_keys, indent=indent)))
    except Exception as e:
        #There's not much to be done since the database is corrupted. Just close the file and exit
        f.close()
        sys.exit()
    f.close()

f = open('conf.json','r')
data = f.read()
conf = json.loads(data)
Shift = int(conf['Shift'])
Loads = conf['Loads']
f.close()

db = {}

if (os.path.exists(Loads)==False):
    db = '{"tickets":[]}' #default structure of the json database
    f = open(Loads,'x')
    f.write(cypher(db))
    f.close()
    
f = open(Loads,'r')
data = f.read()
clean = decypher(data)
db = json.loads(clean)
f.close()


print(db)

@app.route('/api/kanban',methods=['GET', 'POST', 'PUT'])
def kanban_request():
    res = {}
    print(request.get_data())
    if request.method == 'GET':
        return json.dumps(db,sort_keys=sort_keys, indent=indent) # This part of the spec is a little vague, so I just went for a json response
        
    elif request.method == 'POST':
        task = {}
        task["uuid"] = request.form["uuid"]
        task["state"] = request.form["state"]
        for t in db["tickets"]:
            if t["uuid"]==task["uuid"]:
                t["state"] = task["state"]
        
        save(db)
        
        res["code"] = 200
        res["msg"] = "Task modified successfully"
        
        
    elif request.method == 'PUT':
        task = {}
        task["state"] = "backlog"
        task["description"] = request.form["description"]
        task["user"] = request.form["user"]
        task["date"] = datetime.now().strftime("%d %b %Y")
        task["uuid"] = str(uuid.uuid4())
        db["tickets"].append(task)
        
        save(db)
        
        res["code"] = 201
        res["msg"] = "Task created successfully"
        
    else:
        res["code"] = 405
        res["msg"] = "Method not allowed"
    return json.dumps(res,sort_keys=sort_keys, indent=indent)

    
if __name__  == "__main__":
    app.run(host=os.getenv('HOSTIP','0.0.0.0'),port=os.getenv('PORT',23456),debug=bool(os.getenv('FLASKDEBUG',False)))
    
    