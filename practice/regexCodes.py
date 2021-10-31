import re

# regex code with inner description of parameters
pattern = r"(?P<outcode>[A-Za-z][A-Za-z0-9]{1,2}[A-Za-z0-9]?)[ ](?P<incode>"
pattern += "([0-9][A-Za-z^CIKMOV][A-Za-z^CIKMOV]))$"

# some valid codes
testsOk = "M1 1AA", "M60 1NW", "CR2 6XH", "DN55 1PT", "W1A 1HQ", "EC1A 1BB"

# some invalid codes
testsFail = " ", "  ", "   ", "        ", "M1  1AA", "M6 0 1NW", "CR2 A6XH",
"DN55A 1PT", "W 1A 1HQ", "EC 1A 1B", "CR2AA6XH", "CR2A6XH"

# test cases for accepted codes
for test in testsOk:
    print(f"testing ok: '{test}' - Result: {re.match(pattern,test) != None}")

# test cases for failing codes
for test in testsFail:
    print(f"testing fail: '{test}' - Result: {re.match(pattern,test) != None}")
