# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_month = 0
extra_payment_start_month = int(input('What month do you want to start making extra payments?: '))
extra_payment_end_month = int(input('What month do you want to end making extra payments?: '))
extra_payment = int(input('How much extra do you want to pay?: '))

while principal > 0 and payment_month < extra_payment_start_month:
    principal = principal * (1+rate/12) - payment
    payment_month = payment_month + 1
    total_paid = total_paid + payment
    print('Month', payment_month, 'Total paid', round(total_paid, 2), 'Principal', round(principal, 2))

while principal > 0 and payment_month >= extra_payment_start_month and payment_month <= extra_payment_end_month:
    principal = principal * (1+rate/12) - payment - extra_payment
    payment_month = payment_month + 1
    total_paid = total_paid + payment + extra_payment
    print('Month', payment_month, 'Total paid', round(total_paid, 2), 'Principal', round(principal, 2))

while principal > 0 and payment_month > extra_payment_end_month:
    principal = principal * (1+rate/12) - payment
    payment_month = payment_month + 1
    total_paid = total_paid + payment
    print('Month', payment_month, 'Total paid', round(total_paid, 2), 'Principal', round(principal, 2))

#print('Total paid', round(total_paid, 2))
#print('Months', payment_month)
print(f'${total_paid:.2f} paid over {payment_month} months')