from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>git 
        <style>
            form {
                backgorund-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;

            }
        </style>
    </head>
    <body>
        <!-- create your form hereS -->
        
   
        <form method="post">
            <label for="text"><strong>Rotate by:</strong></label>
            <input type="textarea" name="text"/>
            <input type="submit" name="Summit Query" />
    

        </form>

    </body>
</html>

        """
@app.route("/")
def index():
    return form

app.run()


#@app.route("/")
#def encrypt():
    #print ("Success!")





