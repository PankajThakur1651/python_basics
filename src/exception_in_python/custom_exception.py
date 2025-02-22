import logging

allowed_amount = 10000
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

class OverTheLimitException(Exception):
    def __int__(self, msg):
        self.msg = msg


def Withdrawl(amount):
    if amount > allowed_amount:
        raise OverTheLimitException("You can not Withdraw more then 10000 Rupees Per day ")
    else:
        return ""

try:
    if print(Withdrawl(15000)) is None:
        print("Withdrawal allowed")
except OverTheLimitException as exce:
    logging.error(f"Exception {exce}")
finally:
    print("Cleanup here if required")
