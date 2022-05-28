# Implementation Documentation for Keystroke Authentication API
This repository contains codes for keystroke authentication API, keystrokes logger and the swagger API documentation.

<br>
<h2><strong> Keystroke Authentication API</strong></h2>
The keystroke authentication api is the official api for interfacing with our keystrokes dynamics authentication which is built with Flask.
<h3><Strong>Retrieving Secrets From Google Secret Manager</strong></h3>

We wrote a function that calls the `secret.py` file to retrieve secrets as shown below.
<!-- Secrets are retrieved from the Google Secret Manager using the secret.py file through our function below. -->

```python
from secret import GoogleSecret
def getSecrets(key1, key2):
    result = GoogleSecret.get_all()
    secret1, secret2 = result.get(key1), result.get(key2)
    return secret1, secret2
```

Basically, we would be retrieving two secrets from Google Secret Manager. First is the `salt_iv_B` and the second is `DB_password`. This function is called in our code as shown below:

```python
salt_iv_B_key = ''
db_key = ''
salt_iv_key, DB_password = getSecrets(salt_iv_B_key, db_key)
```

<h3><Strong>Setting Up Flask, Database Connection and Celery</strong></h3>

The API was built with `Flask` running with `MYSQL` database and `Celery` was used for storing data into the database asynchroneously. It is important to update the `DB_name`, `DB_user` and `host` in order to establish a connection to the database.

```python
app = Flask(__name__)
DB_name = 'soteria'
DB_user = 'root'
host = 'localhost'
app.config['CELERY_BROKER_URL'] = 'sqla+mysql://'+DB_user+':'+DB_password+'@'+host+'/'+DB_name
app.config['result_backend'] = 'db+mysql://root:'+DB_password+'@'+host+'/'+DB_name
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+DB_user+':'+DB_password+'@'+host+'/'+DB_name
db = SQLAlchemy(app)
```

<h3><Strong>Launching the API</strong></h3>

1. Run the `scan_api.py` file. If at production, you should change `debug=True` to `debug=False` before running the file.
2. To automatically create the database tables, enter the below codes in the terminal.
```
export FLASK_APP=keystroke_auth_api
flask shell
from scan_api import db
db.create_all()
```
3. To start Celery background process, type this in the terminal.
```
celery -A keystroke_auth_api.celery worker --loglevel=info
```

<br>
<h2><strong> Keystrokes Logger File</strong></h2>

The `logger.js` file has been provided to unintrusively capture user's keystrokes data while they attempt to login. To use this code, please follow the steps below.

1. Add the line below into the html code. Kindly change the "path" to the path where the logger.js file is.

```html
<script src="<path>/logger.js"></script>
```

2. For the `logger.js` script to work, these IDs must be used for the username, password and the form: `login_form`, `username` and `pwd`. See example below.

 ```html
<form id="login_form" method="POST">
    <input type="text" id="username" name="username" placeholder="Username">
    <input type="password" id="pwd" name="pwd" placeholder="Password">
    <input type="submit" id="login" value="Login">
</form>
 ```

 3. You can add code to make POST request to Gluu endpoint in the function below. The captured user's keystrokes data can be accessed with the variable name `k_data` in the function. This function can be found in the `logger.js` file. 

 ```javascript
 // Handle the login form submit
lform.onsubmit = function() {
    k_data = getKeystrokesData() // User's keystrokes data
    // ... Add codes to send POST request to Gluu endpoint if neccessary
};
```
<br>

<h2><strong> Swagger API Documentation</strong></h2>

The Swagger api documentation can be found here https://8f1e-67-249-20-200.ngrok.io/swagger_api/.


