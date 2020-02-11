from flask import Flask,request
import os
from werkzeug.utils import secure_filename

UPLOAD = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg'])



app = Flask(__name__)
app.config['UPLOAD'] = UPLOAD

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['files']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
            return '{} upload successed~'.format(filename)


    return '''
    <!doctype html>
    <title>上传文件</title>
    <h1>上传文件</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=files>
         <input type=submit value=上传>
    </form>
    '''
if __name__ == '__main__':
    app.debug = True
    app.run()
