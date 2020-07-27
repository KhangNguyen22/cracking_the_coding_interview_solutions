def areCharactersUnique(s): 
      
    # An integer to store presence/absence  
    # of 26 characters using its 32 bits 
    checker = 0
      
    for i in range(len(s)): 
          
        val = ord(s[i]) - ord('a') 
        print("intro")
        print(val)
          
        # If bit corresponding to current  
        # character is already set 
        if (checker & (1 << val)) > 0: 
            return False
          
        # set a single bit in checker (e.g. before = 0001, after = 1001)  
        checker |= (1 << val) 
        print("checker: ")
        print(checker)
          
    return True
      
# Driver code 
s = "adc"
if areCharactersUnique(s): 
    print("Yes") 
else: 
    print("No") 