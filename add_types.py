def funky(a , b):
    #while True:
        try:
            if type(a) == int and type(b) == int:
              return(a+b , "Is the sum of ",a, " and ", b)  #sum
            elif type(a) == float and type(b) == float:
              return(a+b, "Is the sum of the two floats")
            elif type(a) == str and type(b) == str:
              return(a+b, "Is the concatenated string of", a, "and", b)
            elif type(a) == list and type(b) == list:
              return(a+b, "Is the concatenated list of", a, "and", b)
            elif type(a) == dict and type(b) == dict:
              #c = a.copy()  #copy whatever's in a, store it in c  ---good too
              #c.update(b)    #add whatever's in b to c  ---good too
              c = dict(a, **b)
              return(c , "is the combined dictionary")
            else:
                return("-----")
                #break
        except ValueError:
            print("Incorrect value")
            #break
        except TypeError:
            print("Incorrect type")
            #break


#test 
print funky(10,20)
print funky("10", "20")
print funky([1,2,3], [10,20,30,40])
print funky({'a': 'pink_lady', 'melon': 'zebra'}, {'animal': 'lion', 'tree':'oak'})