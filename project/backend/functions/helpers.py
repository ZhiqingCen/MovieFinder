import sys
sys.path.append('../')

import config
import jwt
import smtplib
import ssl
import database
from database import users
from send_mail import *


#Any functions that are not executed directly by the api
db = database.db


def genJWT(email):
    enc = jwt.encode({"email": email}, config.JWT_KEY, algorithm="HS256")
    return enc


def decodeJWT(token):
    try:
        data = jwt.decode(token, config.JWT_KEY, algorithms=["HS256"])
        return data
    except:
        return None


def sendotc(email, code):
    print(f'email is {email}')
    message = email_confirmation_message(code)
    send_email(email, message, "Confirmation Code")


def expire(mail, otc):
    print("\nexpire")
    # query gives a list of users
    u = users.query.filter_by(email = mail, tmp = 1, otc = otc)
    if u is not None:
        db.session.delete(u[0])
        db.session.commit()



def validate(jwttoken):
    data = jwt.decode(jwttoken, config.JWT_KEY, algorithms=["HS256"])
    email_recv = data['email']

    user = users.query.filter_by(email = email_recv, tmp = 0, token = jwttoken).all()
    if (user):
        return 1

    return 0
