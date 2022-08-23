sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

new_day = 10
sales_w2.append(new_day)

# sales.extend(sales_w1)
# sales.extend(sales_w2)

sales = sales_w1 + sales_w2
# sales.sort
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5

print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# split and join 

msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg)) 


csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(','.join(csv.split(';')).split(':')))
# print(','.join(','.join(csv.split(';')).split(':'))).split(',')
# friends_list = ['Exercise: fill me with names']


friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise



