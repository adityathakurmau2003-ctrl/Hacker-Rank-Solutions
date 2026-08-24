def merge_the_tools(string, k):
   # iterate over string in steps of size k
   for i in range( 0,len(string),k):
    
    sub_string = string[i:i+k]
    
    
    # Remove duplicate character while maintaining order 
    seen = set()
    result =[]
    for char in sub_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
            #print the distinct sub string
    print("".join (result))
        
 
  

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
