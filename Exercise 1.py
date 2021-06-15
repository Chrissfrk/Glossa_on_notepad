#Exercise 1.0
string = str(input("Enter a sentence: ")) 

def reverse(string): 
    words = string.split() 
    r_words = [] 
    for word in words: 
        word = word[::-1]
        r_words.append(word)
    output = " ".join(r_words)
    return output
           

output = reverse(string)
print(output)


