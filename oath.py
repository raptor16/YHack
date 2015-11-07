import hmac
from hashlib import sha256

def generate_sig(endpoint, params, secret):
    sig = endpoint
    for key in sorted(params.keys()):
        sig += '|%s=%s' % (key, params[key])
    return hmac.new(secret, sig, sha256).hexdigest()

endpoint = '/media/657988443280050001_25025320'
params = {
    'access_token': 'fb2e77d.1406078bbd424acc8fc8095f881aa95a',
    'count': 10,
    
}
secret = 'ecd305ad5bc0425db28347e1c5078821'

sig = generate_sig(endpoint, params, secret)
print sig