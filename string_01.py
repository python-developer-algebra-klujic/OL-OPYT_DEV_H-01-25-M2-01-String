first_name = input('Upisite  Vase ime: ')
last_name = input('Upisite  Vase prezime: ')
age = int(input('Upisite  Vasu dob: '))


# 'Dobro dosli! Prijavljeni ste kao ' + last_name + ' ' + first_name + ', (' + age + ').'
# message = 'Dobro dosli! Prijavljeni ste kao {} {}, ({}).'.format(first_name, last_name, age)
message = f'Dobro dosli! Prijavljeni ste kao {last_name.capitalize()} {first_name.capitalize()}, ({age}).'

print(message)
