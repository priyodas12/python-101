from datetime import datetime
# input: 3456-7832-8233-0929:67782.8923:debit,3456-7832-8233-7821:90000.8923:credit
tx_details=input("enter card_number:transaction_amount").split(",")
menu_length=30
tx_status_code="";
for tx_detail in tx_details:
    card_number,tx_amt,tx_status=tx_detail.split(":")
    if tx_status== 'credit':
        tx_status_code="to"
    else:
        tx_status_code="from"
    print(f"""---------Transaction Alert------------
Amount {tx_amt} has been {tx_status}ed 
{tx_status_code} Card Number: {('X' * (4) +"-")*3+ card_number[-4:]}
at {datetime.now()}
--------------------------------------
""")

