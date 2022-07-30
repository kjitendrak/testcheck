class bank:

    def transaction(self):
        print("total tranc")
    def account_open(self):
        print("account status")
    def deposite(self):
        print("deposite amount")

class hdfc_bank(bank):
    def hdfc2icici(self):
        print("transactio to icici")

class icici(hdfc_bank):
    pass
abc=icici()
abc.hdfc2icici()
abc.deposite()
abc.transaction()
#icici.transaction(self)