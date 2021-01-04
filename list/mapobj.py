import random


txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
    
final_prices = map(get_price_with_tax, txns)
final_prices_comp = [get_price_with_tax(i)  for i in txns]

print(list(final_prices_comp),end = '\n\n')

sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'

def is_consonant(letter):
    return letter.isalpha() and letter not in 'aeiou'

consonants = [l for l in sentence if is_consonant(l)]
consonants_unique = {l for l in sentence if is_consonant(l)}

print (consonants,end = '\n\n')
print (consonants_unique,end = '\n\n')

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

def get_weather_data():
    return random.randrange(90, 110)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps,end='\n\n')

cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
matrix = [[i for i in range(5)] for _ in range(6)]
temps = {city: matrix for city in cities}
print(temps,end ='\n\n')


# print(matrix,end = '\n')





