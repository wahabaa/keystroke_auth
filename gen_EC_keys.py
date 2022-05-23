import os
import hashlib
from google.cloud import secretmanager
from binascii import hexlify, unhexlify
from ecdsa import SigningKey, NIST256p

def create_secret(project_id, secret_id):
    client = secretmanager.SecretManagerServiceClient()
    parent = f"projects/{project_id}"
    secret = {'replication': {'automatic': {}}}
    # Create the secret
    response = client.create_secret(secret_id=secret_id, parent=parent, secret=secret)
    # Print the new secret name.
    print(f'Created secret: {response.name}')


def add_secret_version(project_id, secret_id, payload):
    client = secretmanager.SecretManagerServiceClient()
    parent = f"projects/{project_id}/secrets/{secret_id}"
    payload = payload.encode('UTF-8')
    response = client.add_secret_version(parent=parent, payload={'data': payload})
    # Print the new secret version name.
    print(f'Added secret version: {response.name}')  


# Create the secret------------------------------------------------
create_secret('soteria-private-key', 'EC_keys')
#------------------------------------------------------------------

# Generate the EC key-pairs
B = SigningKey.generate(curve=NIST256p)
B_string = B.to_string()
vk = B.verifying_key
salt = os.urandom(16)
iv = os.urandom(16)
secret = "%s-%s-%s" % (hexlify(salt).decode("utf8"), hexlify(iv).decode("utf8"), hexlify(B_string).decode("utf8")) # Salt_iv_B

#------------------------------------------------------------------
# Store signing key (salt_iv_B) in Google Secret Manager
add_secret_version('soteria-private-key', 'EC_keys', secret)
# Store verifying key in Google Secret Manager
add_secret_version('soteria-private-key', 'EC_keys', hexlify(vk.to_string()).decode("utf8"))
#------------------------------------------------------------------