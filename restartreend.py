import re

testString = input()
substring = input()

mo = re.search(substring + '+?', testString)

start = mo.start()
end = mo.end()

tupleResult = (start, end)

print(tupleResult)