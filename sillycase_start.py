
def sillycase(silly):
            print silly
            if (len(silly) % 2 == 0):
              leng = (len(silly)) / 2 
              print leng
            else:
              leng = (len(silly) / 2)
              print leng
              
            

sillycase('foobar') # "fooBAR")
sillycase('codewars') # "codeWARS")
sillycase('brian') # 'briAN')

