with open ('day9input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def validate(x, preamble):
    '''2 pointer technique to find i,j in prev 27 which sum to x '''
    p = sorted([int(i) for i in preamble]) #convert unordered str list to ordered int list
    validated = False


    for i in range(len(p)):
        for j in range(len(p)):

            if p[i] + p[j] == int(x) and i!=j:
                validated=True #exists i, j in prev 27 which sum to x

            elif p[i] + p[j] > int(x):
                break #list ordered so no more possibilities

    if validated == False:
        print ('{} is not valid' .format(x))
        return(x) #return invalid num



def findSet(x, data):

    d = [int(i) for i in data]

    for i in range(len(d)):
        set = [d[i]]
        sum = d[i]
        for j in range(len(d)):

            if i!=j and j>i:
                #print( str(d[i]) + str(d[j]) )
                sum += d[j]
                set.append(d[j])
                #print('sum = {}' .format(sum) )

                if sum == int(x):
                    #print('set = {}' .format(set) )
                    return (set)

                elif sum > int(x):
                    #print ('sum = {}, >{}, no set found' .format(sum, x) )
                    break






for n in range(27, len(data)): #(preamble len, whole len)
    validated = validate (data[n], data[ n-27 : n]) #(test num, previous nums (len preamble) )

    if validated != None:
        invalidNum = validated

set = findSet(invalidNum, data) #part 2

weakness = max(set) + min(set)

print('weakness = {} + {} = {}' .format( max(set), min(set), weakness ) )
