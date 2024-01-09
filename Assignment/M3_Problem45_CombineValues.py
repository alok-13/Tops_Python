# Import the 'Counter' class from the 'collections' module.
from collections import Counter


d1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = Counter()

for i in d1:
    # Update the 'result' Counter by adding the 'amount' to the corresponding 'item' key.
    result[i['item']] += i['amount']

# Print the 'result' Counter, which contains the summed amounts for each 'item'.
print(result) 

            
