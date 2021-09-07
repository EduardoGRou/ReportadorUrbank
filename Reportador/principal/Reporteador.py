from principal.models import User,Pagos,TipoInversion

def showCoins(usrID):
    count= TipoInversion.objects.count()
    user= User.objects.get(id=usrID)
    if (user.id > 0):
        for n in range(1,count+1):
            wallet=TipoInversion.objects.get(id=n)
            if (user.id*-1==wallet.toWhom):
                '''showCoins.Donde=wallet.donde
                showCoins.Dollars=wallet.dollars
                showCoins.Euros=wallet.euros
                showCoins.Shivas=wallet.shivas
                showCoins.Ethers=wallet.ethers
                showCoins.Bitcoins=wallet.bitcoins
                showCoins.Cardanos=wallet.cardanos'''
                showCoins.coinsarr[n-1][0]=wallet.donde
                showCoins.coinsarr[n-1][1]=wallet.dollars
                showCoins.coinsarr[n-1][2]=wallet.euros
                showCoins.coinsarr[n-1][3]=wallet.shivas
                showCoins.coinsarr[n-1][4]=wallet.ethers
                showCoins.coinsarr[n-1][5]=wallet.bitcoins
                showCoins.coinsarr[n-1][6]=wallet.cardanos

            else:
                '''showCoins.Donde="404:_investment_entry_not_found"
                showCoins.Dollars="404:_investment_entry_not_found"
                showCoins.Euros="404:_investment_entry_not_found"
                showCoins.Shivas="404:_investment_entry_not_found"
                showCoins.Ethers="404:_investment_entry_not_found"
                showCoins.Bitcoins="404:_investment_entry_not_found"
                showCoins.Cardanos="404:_investment_entry_not_found"'''
    else:
        '''showCoins.Donde="User_doesn't_have_a_investment"
        showCoins.Dollars="User_doesn't_have_a_investment"
        showCoins.Euros="User_doesn't_have_a_investment"
        showCoins.Shivas="User_doesn't_have_a_investment"
        showCoins.Ethers="User_doesn't_have_a_investment"
        showCoins.Bitcoins="User_doesn't_have_a_investment"
        showCoins.Cardanos="User_doesn't_have_a_investment"'''
