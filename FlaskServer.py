from flask import  Flask, send_from_directory
import socket
import os
import sys


app = Flask(__name__)

try:
    PORT = sys.argv[1]
except IndexError:
    PORT = 5000

try:
    PATH = sys.argv[2]
except IndexError:
    PATH = os.getcwd()


l = os.listdir(PATH)
html = """
<!-- index.html -->


<!DOCTYPE html>

<html lang="en">
<body>
  <style>
  a:link, a:visited {
  background-color: white;
  color: black;
  border: 2px solid green;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: green;
  color: white;
}
</style>"""
for f in l:
    html += f"<a href='{f}'>{f}</a><br>"
 
html += "</body></html>"



@app.route('/')
def main():
    os.chdir(f"{PATH}")
    return html


app.config['files'] = PATH
@app.route('/<filename>')
def send_file(filename):
    print(filename)
    return send_from_directory(app.config['files'], filename=filename, as_attachment=True)



if __name__ == '__main__':
    app.run(f'{socket.gethostbyname(socket.gethostname())}', port=PORT)