from sys import argv

script_name, production, rate, premium = argv


def worker_pay(x, y, z):
    pay = (x * y) + z
    return pay


a = worker_pay(int(production), int(rate), int(premium))
print("You need to pay your worker, dollars: ", a)
