from .models import UrbUser, User, Pagos, TipoInversion


def saveUser(usrID):
    urbUser = UrbUser.objects.get(uid=usrID)
    firstname=urbUser.firstname
    lastname= urbUser.lastname
    user=User(id=usrID,name= firstname+" "+lastname)
    user.save()

def savePagos(usrID): 
    pago=Pagos(id=usrID, toWhom=usrID*-1)
    pago.save()

def saveInver(usrID):
    urbUser = UrbUser.objects.get(uid=usrID) 
    inver=TipoInversion(id=usrID, toWhom=usrID*-1, donde="Crypto")
    inver.save()

