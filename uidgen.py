# Get timestamp and generate a unique id by ASCII code of timestamp
# Accepts only 65 - 90 and 97 - 122 ASCII codes for generating unique id
# If the digit is even, it will be converted to uppercase letter
# If the digit is odd, it will be converted to lowercase letter

import time

counter = 0

def generate_unique_id():
    global counter
    timestamp = str(float(time.time()))
    
    unique_id = []
    
    for digit in timestamp:
        if digit == '.':
            num = counter
        else:
            num = int(digit)
        
        if num % 2 == 0:
            ascii_code = 65 + (num % 26)
        else:
            ascii_code = 97 + (num % 26)
        
        unique_id.append(chr(ascii_code))

        counter += 1
    return ''.join(unique_id)

for i in range(100):
    print(generate_unique_id())