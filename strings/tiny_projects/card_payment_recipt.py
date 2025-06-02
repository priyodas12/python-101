from datetime import datetime
# input: 3456-7832-8233-0929:67782.8923:debit,3456-7832-8233-7821:90000.8923:credit
tx_details=input("enter card_number:transaction_amount").split(",")
menu_length=30

for tx_detail in tx_details:
    card_number,tx_amt,tx_status=tx_detail.split(":")
    print(f"""---------Transaction Alert------------
Amount {tx_amt} has been {tx_status}ed 
from Card Number: {card_number}
at {datetime.now()}
--------------------------------------
""")

