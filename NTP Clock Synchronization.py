import ccxt
import time


#gpt way
# Initialize Binance exchange
exchange = ccxt.binance()

# Get server time from Binance
server_time = exchange.fetch_time()
print(f"Server time: {server_time}")





#local time
local_time = int(time.time() * 1000)  # Convert to milliseconds
print(f"Local time: {local_time}")



#difference
time_difference = server_time - local_time
print(f"Time difference (ms): {time_difference}")
