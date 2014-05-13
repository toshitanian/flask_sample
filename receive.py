from flask import (Flask, request, render_template)
import os.path
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    image = request.files["image"]
    data = image.stream.read()
    filename = image.filename
    print filename
    (_, ext) = os.path.splitext(filename)
    with open('test.jpg', 'wb') as f:
        f.write(data)
    return ''


@app.route('/web_page')
def web_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# test command
# curl -F image=@sample.jpg http://localhost:5000/ -XPOST
