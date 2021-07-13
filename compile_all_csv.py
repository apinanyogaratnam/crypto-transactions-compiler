from read_csv_shakepay import *
from read_csv_newton import *

newton_data = get_data_newton()
newton_trade_transactions = newton_data[2]

newton_purchase_data = get_purchases_newton(newton_trade_transactions)
newton_purchase_total_bitcoin = newton_purchase_data[0]
newton_bitcoin_received = newton_purchase_data[1]
newton_purchase_total_ethereum = newton_purchase_data[2]
newton_ethereum_received = newton_purchase_data[3]
newton_purchase_total_litecoin = newton_purchase_data[4]
newton_litecoin_received = newton_purchase_data[5]
newton_purchase_total_usdc = newton_purchase_data[6]
newton_usdc_received = newton_purchase_data[7]

shakepay_data = get_data_shakepay()
shakepay_purchase_transactions = shakepay_data[1]

shakepay_purchase_data = get_purchases_shakepay(shakepay_purchase_transactions)
shakepay_purchase_total_bitcoin = shakepay_purchase_data[0]
shakepay_bitcoin_received = shakepay_purchase_data[1]
shakepay_purchase_total_ethereum = shakepay_purchase_data[2]
shakepay_ethereum_received = shakepay_purchase_data[3]

total_spent_on_bitcoin = newton_purchase_total_bitcoin + shakepay_purchase_total_bitcoin
total_bitcoin_received = newton_bitcoin_received + shakepay_bitcoin_received

total_spent_on_ethereum = newton_purchase_total_ethereum + shakepay_purchase_total_ethereum
total_ethereum_received = newton_ethereum_received + shakepay_ethereum_received

print("Total spent on bitcoin: ", total_spent_on_bitcoin)
print("Total bitcoin received: ", total_bitcoin_received)

print("Total spent on ethereum: ", total_spent_on_ethereum)
print("Total ethereum received: ", "{:.9f}".format(total_ethereum_received))