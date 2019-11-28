import random
import string
def randomString(stringLength=20):
    """Generate a random string of fixed length """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))
#print ("Random String is ", randomString() )
#print ("Random String is ", randomString(10) )
#print ("Random String is ", randomString(10) )
