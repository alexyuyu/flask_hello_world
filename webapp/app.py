import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    log('Hello '+provider+'!\n')
    return 'Hello '+provider+'!'

def log(msg):
    print(msg)
    print(os.path.abspath('.'))
    fileObj = open(os.path.abspath('.')+'/app.log','a')
    try:
        fileObj.write(msg)
	print('after writing ',msg)
    except:
        print('got exception!')
    finally:
        fileObj.close()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    print('port:'+port)
    app.run(host='0.0.0.0', port=port)
