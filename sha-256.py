import hashlib
import random
def toSHA256(s):

   return str(hashlib.sha256(s).hexdigest())
   