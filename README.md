# Implementation Documentation for scan_api
This repository contains codes for the EC key-pair generation, Scan API, keystrokes logger and the swagger API documentation.

<h2><strong> EC Key-Pair Generation</strong></h2>
The code below creates a new secret in Google Secret Manager programmatically. Alternatively, a new secret can be created using the Google Secret Manager console.

```python
create_secret('soteria-private-key', 'EC_keys')
```

Therefter, an elliptic curve key-pair is generated for signing and verifying signed data using the below code, alongside with the salt and iv. Note that the salt and iv are generated once and stored together with the signing key (known as B) in the format `salt-iv-B`.

```python
# Generate the EC key-pairs
B = SigningKey.generate(curve=NIST256p)
B_string = B.to_string()
vk = B.verifying_key
salt = os.urandom(16)
iv = os.urandom(16)
secret = "%s-%s-%s" % (hexlify(salt).decode("utf8"), hexlify(iv).decode("utf8"), hexlify(B_string).decode("utf8")) # Salt_iv_B
```

These keys are stored into Google Secret Manager with the code below.

```python
# Store signing key (salt_iv_B) in Google Secret Manager
add_secret_version('soteria-private-key', 'EC_keys', secret)
# Store verifying key in Google Secret Manager
add_secret_version('soteria-private-key', 'EC_keys', hexlify(vk.to_string()).decode("utf8"))
```

<br>
<h2><strong> Scan API</strong></h2>
The scan api is the official api for interfacing with our keystrokes dynamics authentication which is built with Flask.
<h3><Strong>Setting Up The Google Secret Manager</strong></h3>
The parameters used in the code as shown below are only for testing purposes and should be changed or updated before deployment.

```python
project_id = 'soteria-private-key'
key_id = 'EC_keys'
DB_pwd_id = 'DB_Password'
key_version = "2"
db_pwd_version = "1"
```

The `project_id` can be found on the Google Secret Manager console. The `key_id` and `DB_pwd_id` represents the chosen secret name for storing secrets (in this case, the signing key and DB password), while `key_version` and `db_pwd_version` are the version number for the secrets. In case of doubt, these chosen value can be found via the Google Secret Manager console.

The code below calls the Google Secret Manager to retrieve the signing key and Database password.

```python
salt_iv_key, DB_password = access_secret_version(project_id, key_id, DB_pwd_id, key_version, db_pwd_version)
```

To use the Google Secret Manager, you need to set the `GOOGLE_APPLICATION_CREDENTIALS` with the code below. The json file that can be downloaded from the console. Remember to change the path to the json file.

```
export GOOGLE_APPLICATION_CREDENTIALS = "/Users/anumighty/soteria-private-key-849f3d258a44.json"
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
export FLASK_APP=scan_api
flask shell
from scan_api import db
db.create_all()
```
3. To start Celery background process, type this in the terminal.
```
celery -A scan_api.celery worker --loglevel=info
```

<br>
<h2><strong> Keystrokes Logger File</strong></h2>

The `logger.js` file has been provided to unintrusively captures user's keystrokes data while they attempt to login. To use this code, please follow the steps below.

1. Add the line below into the html code. Kindly change the "path" to the path where the logger.js file is.

```html
<script src="<path>/logger.js"></script>
```

2. Ensure these IDs are used for the username, password and the form:
 For the `logger.js` script to work, these IDs must be used for the username, password and the form: `login_form`, `username` and `pwd`. See example below.

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
    k_data = getKeystrokesData()
    // ... Add codes to send POST request to Gluu endpoint if neccessary
};
```
<br>

<h2><strong> Swagger API Documentation</strong></h2>

Please look into the `scan_api_documentation` folder for the API endpoints, the parameters that each endpoint takes and their responses.


