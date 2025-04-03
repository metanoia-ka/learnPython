import json

with open("transactions.json") as trans:
    transactions = json.load(trans)
    
    trans_max = max(transactions, key=lambda x: x["transaction"])
    
    print(f"🏆 La plus grande transaction est de {trans_max['transaction']}€ par {trans_max['nom']}.")