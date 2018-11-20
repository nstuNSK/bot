def get_user():
    f = open('system/base.txt')
    line = f.read(4)
    return line

def get_password():
    f = open('system/base.txt')
    line = f.readline()
    line = f.read(10)
    return line

def get_token():
    f = open('system/token.txt')
    line = f.readline()
    return line

def get_nstu_url():
    f = open('system/api.nstu.txt')
    line = f.readline()
    return line
