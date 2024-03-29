

def calcula_media(v): # v é uma variável local
    print ("Dentro antes")
    print (v)
    v = 10
    print ("Dentro depois")
    print (v)
if __name__=='__main__':
    v = 4 
    calcula_media(4)
    print (v)
