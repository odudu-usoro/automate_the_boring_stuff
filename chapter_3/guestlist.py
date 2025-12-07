guests = ['Jesus', 'Ronaldo', 'Zuckerberg', 'Hitler', 'Mandela']

guest_cancel = guests.pop()
print(f"hey, {guest_cancel} could not make it for dinner\n")

guests.append('Obama')

guests.insert(0, 'Deng Xiaoping')
guests.insert(2, 'Lee Kwan Yu')
guests.insert(4, 'Wole Soyinka')

print(f'I can only have 2 people for dinner')

print(f'hey {guests[0]}, you are still invited')
print(f'hey {guests[1]}, you are still invited')

guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()

guests.remove('Deng Xiaoping')
guests.remove('Jesus')

print(guests)
print(len(guests))