import time
import logging
import requests
from flask import Flask, jsonify, request, render_template, session
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import json
import time
import hashlib
from google.cloud import secretmanager
from binascii import hexlify, unhexlify
from ecdsa import SigningKey, NIST256p
import lzma
from binascii import hexlify, unhexlify
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from math import floor
from math import sqrt
from secret import GoogleSecret


# Get Salt_iv_B and DB Password from Google Secret Manager ---------------------------------------
'''
This code gets Salt_iv_B and DB Password from Google Secret Manager
through the secret.py file
Args: 
    secret_key: salt_iv_B key
    db_key: DB key

Returns: salt_iv_key and DB_password
'''
def getSecrets(key1, key2):
    result = GoogleSecret.get_all()
    secret1, secret2 = result.get(key1), result.get(key2)
    return secret1, secret2
#------------------------------------------------------------------------------------------------


# Call function to retrive secrets only once-----------------------------------------------------
salt_iv_B_key = ''
db_key = ''
salt_iv_key, DB_password = getSecrets(salt_iv_B_key, db_key)
# -----------------------------------------------------------------------------------------------


# Set up FLASK, Database Connection and Celery --------------------------------------------------
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
# ----------------------------------------------------------------------------------------


# Keystroke Algorithm------------------------------------------
def ttwbvgf (O0O000OO0OOO000OO ):
    O0O00O00OO0O000OO =[OOOO000OOOO0O00OO for OOOO000OOOO0O00OO in O0O000OO0OOO000OO if OOOO000OOOO0O00OO [2 ]==0 ]
    O00O0OO0OO0OO0OOO ={}
    for O0O0OOO0OOOOO0OOO in range (len (O0O00O00OO0O000OO )-1 ):
        O0O0O0O0O0O0OO0OO =str (O0O00O00OO0O000OO [O0O0OOO0OOOOO0OOO ][1 ])+'-'+str (O0O00O00OO0O000OO [O0O0OOO0OOOOO0OOO +1 ][1 ])
        if str (O0O00O00OO0O000OO [O0O0OOO0OOOOO0OOO ][1 ])=='Backspace'or str (O0O00O00OO0O000OO [O0O0OOO0OOOOO0OOO +1 ][1 ])=='Backspace':
            continue
        OO0000O0O0O00O00O =O0O00O00OO0O000OO [O0O0OOO0OOOOO0OOO +1 ][0 ]-O0O00O00OO0O000OO [O0O0OOO0OOOOO0OOO ][0 ]
        if 30 <=OO0000O0O0O00O00O <=1000 :
            O00O0OO0OO0OO0OOO .setdefault (O0O0O0O0O0O0OO0OO ,[])
            O00O0OO0OO0OO0OOO [O0O0O0O0O0O0OO0OO ].append (OO0000O0O0O00O00O )
    OO0OO00O000000O0O =[]
    for O0O0OOO0OOOOO0OOO in O00O0OO0OO0OO0OOO :
        if len (O00O0OO0OO0OO0OOO [O0O0OOO0OOOOO0OOO ])>=4 :
            OO0OOO0OO000O000O =sum (O00O0OO0OO0OO0OOO [O0O0OOO0OOOOO0OOO ])*1.0 /len (O00O0OO0OO0OO0OOO [O0O0OOO0OOOOO0OOO ])
            O00OO0000O000O0OO =sqrt (sum ((O0OOO00000OOOOO00 -OO0OOO0OO000O000O )**2 for O0OOO00000OOOOO00 in O00O0OO0OO0OO0OOO [O0O0OOO0OOOOO0OOO ])/len (O00O0OO0OO0OO0OOO [O0O0OOO0OOOOO0OOO ]))
            OO0OO00O000000O0O .append ((O0O0OOO0OOOOO0OOO ,OO0OOO0OO000O000O ,O00OO0000O000O0OO ))
    return OO0OO00O000000O0O 
def qpuyt (OO0O0000OOOO0OO0O ):
    OOO0O0000OOOOOOOO =[OO00O0O0O00OOO0OO for OO00O0O0O00OOO0OO in OO0O0000OOOO0OO0O if OO00O0O0O00OOO0OO [2 ]==0 ]
    O0OOOO00O00OO00O0 ={}
    for O000O0O0O0O0OO0OO in range (len (OOO0O0000OOOOOOOO )-1 ):
        O0000OO00000OO0OO =str (OOO0O0000OOOOOOOO [O000O0O0O0O0OO0OO ][1 ])+'-'+str (OOO0O0000OOOOOOOO [O000O0O0O0O0OO0OO +1 ][1 ])
        if str (OOO0O0000OOOOOOOO [O000O0O0O0O0OO0OO ][1 ])=='Backspace'or str (OOO0O0000OOOOOOOO [O000O0O0O0O0OO0OO +1 ][1 ])=='Backspace':
            continue 
        OOOOO0O0OO0000O00 =OOO0O0000OOOOOOOO [O000O0O0O0O0OO0OO +1 ][0 ]-OOO0O0000OOOOOOOO [O000O0O0O0O0OO0OO ][0 ]
        if 30 <=OOOOO0O0OO0000O00 <=1000 :
            O0OOOO00O00OO00O0 .setdefault (O0000OO00000OO0OO ,[])
            O0OOOO00O00OO00O0 [O0000OO00000OO0OO ].append (OOOOO0O0OO0000O00 )
    return O0OOOO00O00OO00O0 
def axfcafgca43vchc (OO0OO00O00OOOOOO0 ,O0O0000O0O0O000O0 ):
    OO0OO00O00OOOOOO0 =ttwbvgf (OO0OO00O00OOOOOO0 )
    O0O0000O0O0O000O0 =qpuyt (O0O0000O0O0O000O0 )
    return ywbw7224dp (OO0OO00O00OOOOOO0 ,O0O0000O0O0O000O0 )
def ywbw7224dp (O0OOO0O00OO00O000 ,OO0000OO0OOO00O0O ):
    OO0OO0O00OO000O00 ,OOOOOOOO0O00O00O0 ,OOO00O0OOO0OO0O00 =0 ,0 ,0 
    for OO0OO0OO0OO00O000 in O0OOO0O00OO00O000 :
        if OO0OO0OO0OO00O000 [0 ]in OO0000OO0OOO00O0O :
            OOO00O0OOO0OO0O00 +=1 
            for O00OOO00O00OOOO0O in OO0000OO0OOO00O0O [OO0OO0OO0OO00O000 [0 ]]:
                if OO0OO0OO0OO00O000 [2 ]!=0.0 :
                    OOOOOOOO0O00O00O0 +=1 
                    OO0OO0O00OO000O00 +=abs (OO0OO0OO0OO00O000 [1 ]-O00OOO00O00OOOO0O )*1.0 /OO0OO0OO0OO00O000 [2 ]
    if OO0OO0O00OO000O00 !=0 and OOOOOOOO0O00O00O0 !=0 :
        return OO0OO0O00OO000O00 /OOOOOOOO0O00O00O0 ,OOOOOOOO0O00O00O0 ,OOO00O0OOO0OO0O00 ,len (O0OOO0O00OO00O000 )
    else :
        return -1 ,OOOOOOOO0O00O00O0 ,OOO00O0OOO0OO0O00 ,len (O0OOO0O00OO00O000 )
# ----------------------------------------------------------------------------------------


# DB MODEL --------------------------------------------------------------------------------
class Keystrokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), nullable=False)
    data = db.Column(db.String(512), default='')
    iteration = db.Column(db.String(64), default='')

class RejectKeys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), nullable=False)
    data = db.Column(db.String(512), default='')
    iteration = db.Column(db.String(1000), default='')
# -----------------------------------------------------------------------------------------


# Get Derived key -------------------------------------------------------------------------
def getAESkey(secret, A): # Derived key
    salt, iv, B_str = map(unhexlify, secret.split('-'))
    B = SigningKey.from_string(B_str, curve=NIST256p)
    signature = B.sign_deterministic(A.encode('utf8'), hashfunc=hashlib.sha256).hex()
    AES_key = hashlib.pbkdf2_hmac("sha256", signature.encode("utf8"), salt, 1000)
    return AES_key.hex(), iv.hex()
# -----------------------------------------------------------------------------------------


# Encypt data with AES before storing in Database------------------------------------------
def encrypt_db_data(data, aes, iv):
    data = data.encode("utf8")
    data = lzma.compress(data)
    encData = aes.encrypt(unhexlify(iv), data, None) # hex object
    return encData.hex() #String data
# ----------------------------------------------------------------------------------------


# Decrypt data from Database--------------------------------------------------------------
def decrypt_db_data(data, A):
    decrypted_data = []
    AES_key, iv = getAESkey(salt_iv_key, A)
    aes = AESGCM(unhexlify(AES_key))
    for row in data:
        decData = aes.decrypt(unhexlify(iv), unhexlify(row.data), None)
        decData = lzma.decompress(decData)
        decData = decData.decode('utf8')
        decrypted_data.append(json.loads(decData))
    return decrypted_data
# ---------------------------------------------------------------------------------------


# BACKGROUND TASKS TO STORE DATA IN DATABASE---------------------------------------------
@celery.task(name='celery_add_keys')
def save_keystrokes(user, sample_data, last_iter, score, status, AES_key, iv):
    aes = AESGCM(unhexlify(AES_key))
    for k in sample_data:
        data = {"kn": k['kn'], "r": k['r'], "ts": k['ts'], "wn": k['wn'], "score":score, "status":status}
        enc_data = encrypt_db_data(json.dumps(data), aes, iv) # Encrypt data with AES before storing to DB
        push = Keystrokes(user=user, data=enc_data, iteration=last_iter+1)
        db.session.add(push)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
    return 'Added to DB successfully!'

@celery.task(name='celery_move_keys')
def movekeystrokes(user, data, last_iter):
    push = Keystrokes(user=user, data=data, iteration=last_iter+1)
    db.session.add(push)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()
    return

@celery.task(name='celery_delete_keys')
def delete_record(user, iter):
    db.session.query(RejectKeys).filter(RejectKeys.user==user, RejectKeys.iteration==iter).delete()
    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()
    return 'Data Deleted successfully!'
    
@celery.task(name='celery_add_reject_keys')
def save_reject_keystrokes(user, sample_data, score, AES_key, iv):
    aes = AESGCM(unhexlify(AES_key))
    try:
        last_data = RejectKeys.query.filter_by(user=user).order_by(RejectKeys.id.desc()).first()
        last_iter = last_data.iteration
    except:
        last_iter = 0
    for k in sample_data:
        data = {"kn": k['kn'], "r": k['r'], "ts": k['ts'], "wn": k['wn'], "score":score}
        enc_data = encrypt_db_data(json.dumps(data), aes, iv)
        push = RejectKeys(user=user, data=enc_data, iteration=int(last_iter)+1)
        db.session.add(push)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
    return 'Added to Reject Table successfully!'
# ----------------------------------------------------------------------------------------


# Validate Endpoint ------------------------------------------------------------------------
@app.route('/validate', methods=['GET','POST'])
def validate():
    start = time.time()
    if request.method == 'POST':
        user, threshold = '', 0.6
        posted_data = request.get_json()
        '''Get user ID and customer key and keystroke data'''
        try:
            sample = json.loads(posted_data['k_data'])
            user = str(posted_data['user'])
            A = str(posted_data['customer_key'])
        except Exception as e:
            return {'error':'Invalid input', "code":401}
        
        if len(sample) < 1: # No keystroke data
            return {'error':'Invalid input', "code":401}
        if user != '': # Check if user exist in db
            last_data = Keystrokes.query.filter_by(user=user).order_by(Keystrokes.id.desc()).first()
            if last_data is None: # It's first attempt
                # Get the derived AES key
                AES_key, iv = getAESkey(salt_iv_key, A)
                # Add first attempt keystrokes data to Database
                save_keystrokes.delay(user, sample, 0, 0.0, 'building_template', AES_key, iv)
                resp = {"user": user,"status": 'building template', "code":200}
                print('User not in DB and now added.\n-> Time:', time.time() - start)
                return  resp
            else:   # Not the first attempt
                last_iter = int(last_data.iteration)
                if last_iter < 5:   # Add keystrokes to DB
                    # Get the derived AES key
                    AES_key, iv = getAESkey(salt_iv_key, A)
                    # Add attempt keystrokes data to Database
                    save_keystrokes.delay(user, sample, last_iter, 0.0, 'building_template', AES_key, iv)
                    resp = {"user": user,"status": 'building template', "code":200}
                    print('User found', time.time() - start)
                    return  resp
                # Get profile from DB
                profile = Keystrokes.query.filter_by(user=user).all()
                # Decrypt data coming from database ------------
                profile = decrypt_db_data(profile, A)
                profile_k1 = sorted([(int(k['ts']), k['kn'], int(k['r'])) for k in profile if 'username' in k['wn'] or 'email' in k['wn']])
                sample_k1 = sorted([(k['ts'], k['kn'], k['r']) for k in sample if 'username' in k['wn'] or 'email' in k['wn']])
                profile_k2 = sorted([(int(k['ts']), k['kn'], int(k['r'])) for k in profile if k['wn'] == 'pwd' or k['wn'] == 'password'])
                sample_k2 = sorted([(k['ts'], k['kn'], k['r']) for k in sample if k['wn'] == 'pwd' or k['wn'] == 'password'])
                #-----------------------------------------------

                # Use Keystroke Algorithm ----------------
                score1, graph_instance1, shared_graphs1, main_graph1 = axfcafgca43vchc(profile_k1, sample_k1) # Username or email
                if score1 == -1:
                    return {'error':'Insufficient data', "code":401}
                score2, graph_instance2, shared_graphs2, main_graph2 = axfcafgca43vchc(profile_k2, sample_k2) # Password
                if score2 == -1:
                    return {'error':'Insufficient data', "code":401}
                total_graph_instance = graph_instance1 + graph_instance2
                w1 = graph_instance1 / total_graph_instance
                w2 = graph_instance2 / total_graph_instance
                dist_score = ((w1 * score1) + (w2 * score2)) * 0.5
                print('Final Score: ', dist_score)
                min_digraph = floor(0.8 * (main_graph1 + main_graph2))  # 80% information shared digraph
                # ----------------------------------------------

                if shared_graphs1+shared_graphs2 >= min_digraph:
                    if dist_score <= threshold: # distance thresholding
                        status = 'approved'
                        code = 200
                        # Add keystrokes to DB
                        AES_key, iv = getAESkey(salt_iv_key, A)
                        save_keystrokes.delay(user, sample, last_iter, dist_score, status, AES_key, iv)
                    else:
                        status = 'denied'
                        code = 400
                        AES_key, iv = getAESkey(salt_iv_key, A)
                        save_reject_keystrokes.delay(user, sample, dist_score, AES_key, iv)
                    resp = {"user": user,"status": status,"code":code}
                    return resp
                else:
                    return {'error':'Insufficient data', "code":401}
        return {'error':'Invalid User ID. Please register first', "code":401}
    return {'welcome': 'Welcome to Keystroke Dynamics Authentication'}



# NOTIFY ENDPOINT: FOR GETIING NOTIFIED IF USER PASSED OTHER 2FA
@app.route('/notify', methods=('GET', 'POST'))
def notify():
    if request.method == 'POST':
        notify_msg = request.get_json()
        '''Get boolean 'isPassed' '''
        try:
            isPassed = notify_msg['isPassed']
            user = notify_msg['user']
            if isPassed:
                # Get the user's last iteration from the reject_keys table
                reject_keys_last_data = RejectKeys.query.filter_by(user=user).order_by(RejectKeys.id.desc()).first()
                if reject_keys_last_data is not None:
                    reject_keys_last_iter = int(reject_keys_last_data.iteration)
                    reject_keys_data = RejectKeys.query.filter_by(user=user, iteration=reject_keys_last_iter).all()
                    # Get the last iteration from Keystrokes table
                    last_data = Keystrokes.query.filter_by(user=user).order_by(Keystrokes.id.desc()).first()
                    last_iter = int(last_data.iteration)
                    # Move the data to Keystrokes table
                    for k in reject_keys_data:
                        movekeystrokes.delay(user, k.data, last_iter)
                    print('Data Moved successfully!')
                    # Delete the data from reject_keys table
                    delete_record(user, reject_keys_last_iter)
                    resp = {"user": user,"status": "Successful","code":200}
                else:
                    resp = {"error": "Nothing to delete","code":401}
                return resp
            else:
                resp = {"error": "Nothing to delete, User failed other MFA","code":401}
                return resp
        except Exception as e:
            resp = {"error": "Wrong data passed!","code":401}
            return resp
    resp = {"error": "Something went wrong!","code":401}
    return resp


# ==============================================================================
if __name__ == '__main__':
    app.run(port=7000, debug=True)
# ==============================================================================