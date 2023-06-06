import random
def hash_func(msg):
    random.seed(msg)
    hash_value=random.randint(0,2**16-1)
    return hash_value
msg=input("Enter the message : ")
hash_value=hash_func(msg)
print("Original Message :",msg)
print("Hash value :",hash_value)

received_msg=input("Enter the received message : ")
received_hash_value=hash_func(received_msg)
print("Received Message :",received_msg)
print("Received Hash value :",received_hash_value)

if received_hash_value==hash_value:
    print("Integrity : The message has not been modified")
else:
    print("Integrity : The message has been modified")