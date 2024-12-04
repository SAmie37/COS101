from operator import index

numericals = [33, 34, 35, 36, 37, 38, 39, 22, 21, 20]

index = 0
while numericals[index:] :
    index += 1
    numericals_index = index -1
    for number in range(numericals_index, -1, -1):

        print(numericals[number])