import re

pattern = r"(?P<outcode>[A-Za-z][A-Za-z0-9]{1,2}[A-Za-z0-9]?)[ ](?P<incode>([0-9][A-Za-z^CIKMOV][A-Za-z^CIKMOV]))$"
sequence = "AA11 AA"
print(re.match(pattern,sequence) != None)

tests="M1 1AA","M60 1NW","CR2 6XH","DN55 1PT","W1A 1HQ","EC1A 1BB"
testsF=" ", "  ", "   ", "        ","M1  1AA","M6 0 1NW","CR2 A6XH","DN55A 1PT","W 1A 1HQ","EC 1A 1B","CR2AA6XH","CR2A6XH"
for test in tests:
    print(f"testing ok: '{test}' - Result: {re.match(pattern,test) != None}")

for test in testsF:
    print(f"testing fail: '{test}' - Result: {re.match(pattern,test) != None}")
