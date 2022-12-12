from touch_id.touchid import authenticate

def logger(reason:str):
    if authenticate(reason=reason) == True:
        return True
    else:
        return False