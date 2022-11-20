# Main Robee Manager System

import mxo
# from RobeeServices import RobeeSystem

import time
DemoSystem = {
    "main": 1111,
    "processA": 1112,
    "processB": 1113,
}

class Main(mxo.MicroXO):
    pass


@Main
def Hello(*args,**kwargs):
    return {"res": " !!! @@@@ Hello from MAIN SERVICE !!!"+str(args) , "args":args,"kwargs":kwargs}


# main = Main().register()
main = mxo.MicroXO.register("Main", _services = DemoSystem ) 

while(True):
    time.sleep(1)


