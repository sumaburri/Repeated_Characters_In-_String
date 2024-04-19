string=input('Enter a String : ')
new_string=''
for ch in string:
    if ch not in new_string:
        new_string+=ch
for char in new_string:
    if string.count(char)>1:
        print(char)
        
   
