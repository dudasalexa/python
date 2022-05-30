import smsmodul

f=open("sms.txt")
sorok=f.read().split("\n")
f.close()

print(sorok)
