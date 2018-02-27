##How to setup
'''sh
virtualenv my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt-- Only first time.
'''

##How to run?
'''sh
FLASK_APP=hello.py flask run
'''

##GET /
'''sh
curl -i http://127.0.0.1:5000/

'''

##POST /users
'''sh
curl -i -X POST http://127.0.0.1:5000/users -d "name=<username>"
curl -i -X POST http://127.0.0.1:5000/users -d "name=foo"
curl -i -X POST http://127.0.0.1:5000/users -d "name=foo1"
curl -i -X POST http://127.0.0.1:5000/users -d "name=foo2"

##GET /users/
'''sh
curl -i http://127.0.0.1:5000/users/
'''

##DELETE /users//
'''sh
curl -i -X DELETE http://127.0.0.1:5000/users/ -d "name=<username>"
curl -i -X DELETE http://127.0.0.1:5000/users -d "name=foo"
  curl -i -X DELETE http://127.0.0.1:5000/users -d "name=foo1"
'''
