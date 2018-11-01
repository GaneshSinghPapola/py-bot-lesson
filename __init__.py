import os,sys
from application import app 

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    HOST = os.environ.get('IP', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host=HOST, port=PORT, debug=True, threaded=True)