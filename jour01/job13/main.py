print('Bonjour vous allez devoir tapez 5 nombres')
print(', '.join(sorted([str(input('Nombre ' + str(i+1) + ' :\n')) for i in range(5)])))