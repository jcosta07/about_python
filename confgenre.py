genre = str (input('insert: ')).strip().upper()
while genre not in 'MmFf':
    genre = str (input('insert again: '))
print ('thank you!')