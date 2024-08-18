def calculate_love_score(name1 : str, name2: str) -> int:
    '''
    Tests the compatibility between two names.  To work out the love score between two people.
    
    * name1 = "Angela Yu" name2 = "Jack Bauer"

    T occurs 0 times 
    
    R occurs 1 time 
    
    U occurs 2 times 
    
    E occurs 2 times 
    
    Total = 5 
    
    L occurs 1 time 
    
    O occurs 0 times 
    
    V occurs 0 times 
    
    E occurs 2 times 
    
    Total = 3 
    
    Love Score = 53
        '''
    final_name = (name1 + name2).lower()
    
    t = 0
    
    r = 0
    
    u = 0
    
    e = 0
    
    l = 0
    
    o = 0
    
    v = 0
    
    for i in final_name:
        
        if i == "t":
            t += 1
        
        if i == "r":
            r += 1
            
        if i == "u":
            u += 1
            
        if i == "e":
            e += 1
            
        if i == "l":
            l += 1
            
        if i == "o":
            o += 1
            
        if i == "v":
            v += 1
            
            
    print(f"T occurs {t} times")
        
    print(f"R occurs {r} times")
        
    print(f"U occurs {u} times")
        
    print(f"E occurs {e} times")
        
    true = t + r + u + e
        
    print(f"Total = {t + r + u + e}")
        
    print(f"L occurs {l} times")
        
    print(f"O occurs {o} times")
        
    print(f"V occurs {e} times")
        
    print(f"E occurs {e} times")
        
    love = l + o + v + e
        
    print(f"Total = {l + o + v + e}")
        
        
    print(f"Love Score = {(true * 10) + love}")
        

    
