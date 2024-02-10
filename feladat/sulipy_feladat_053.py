def legnagyobb_kereso(x, *args):
              """
              egy kötelező paraméter van, és a többi (tetszőlegesen sok)
              paraméter az 'args' nevű listában tárolódik
              """
              legnagyobb = x
              for szam in args:
                    if szam > legnagyobb:
                          legnagyobb = szam
              return legnagyobb
    
    
print(legnagyobb_kereso(1, 19, 11, 7, 17))
    