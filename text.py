handle = open('text.txt','r')

def revword (word):
    str_1=" "
    i = len(word) 
    while i > 0: 
        str_1 =str_1+word[ i - 1 ]
        i = i - 1 
    return str_1.casefold().strip()


def countword() :
    handle = open('text.txt')
    inp=handle.read()
    words=inp.split()
    word=words[0].casefold()
    wordi=words[1:]
    rev=" "
    counter=1
    for i in wordi:
        rev=revword(i).casefold().strip()
        if rev==word:
            counter=counter+1
    return (counter)


print(countword())
   
    
    