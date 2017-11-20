from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form ="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/encrypt "method="post">
        Rotate by: <input type="text" name="rot"> <br>
        <textarea type="text" name="message">{0}</textarea> <br>
        <input type="submit" value="Submit Inquiry">
        </form>
    </body>
</html>
"""


@app.route("/encrypt" , methods=['POST']) 
def encrypt():
    rotation = request.form['rot']
    encrypted_message = request.form['message']
    rotation = int(rotation)
    encrypted_message = str(encrypted_message)
    cypher = rotate_string(encrypted_message, rotation)
    return form.format(cypher)

#Within encrypt, store the values of these 
#request parameters in local variables, 
#converting data types as necessary. Then, encrypt the value 
#of the text parameter using rotate_string. Return the encrypted 
#string wrapped in <h1> tags, to be rendered in the browser.

@app.route("/")
def index():
    return form.format()


app.run()