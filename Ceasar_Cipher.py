
def ceasar():
    print('''                                                                                                                                              
                                                                                                             88                                 
                                                                                                             88                                 
                                                                                                             88                                 
 ,adPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,           ,adPPYba, 8b       d8 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" a8P_____88 ""     `Y8 I8[    "" ""     `Y8 88P'   "Y8          a8"     "" `8b     d8' 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         8PP""""""" ,adPPPPP88  `"Y8ba,  ,adPPPPP88 88                /n  8b          `8b   d8'  88       d8 88       88 8PP""""""" 88          
"8a,   ,aa "8b,   ,aa 88,    ,88 aa    ]8I 88,    ,88 88                  "8a,   ,aa   `8b,d8'   88b,   ,a8" 88       88 "8b,   ,aa 88               
 `"Ybbd8"'  `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"' `"8bbdP"Y8 88                   `"Ybbd8"'     Y88'    88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                         d8'     88                                             
                                                                                        d8'      88                                             
''')  #This Art could be placed outside the ceasar function to avoid it appearing over and over again when calling the ceasar function again, but I didn't like it that way :)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "decode":
        switch = -1
        
    elif direction == "encode":
        switch = 1
    
    
    def locked(text : str, shift : int) -> str:
        
        code = ""
        
        for i in text:
            
            if i == " ":
                code += " "
                
            elif i not in alphabet:
                code += i                
                
            else:
                
                if alphabet.index(i) + (shift * switch) > 25:
                    result = (alphabet.index(i) + (shift * switch) - (26 * switch))
                    code += alphabet[result]
                elif alphabet.index(i) + (shift * switch) < 0:
                    result = (alphabet.index(i) + (shift * switch) - (26 * switch))
                    code += alphabet[result]                    
                else:
                    code += alphabet[alphabet.index(i) + (shift * switch)]
                    
                
        print(f"Here is the {direction}d result: {code}")
    
    locked(text, shift)
                    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n ")
    
    should_continue = True
    
    while should_continue:
        
        if restart == "yes":
            ceasar()            
    
        elif restart == "no":
            print("Goodbye")
            should_continue = False
               
ceasar()           
            
            
