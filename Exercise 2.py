#Exercise 2
phrase = ""
with open("sample.txt", "r") as txt:
        for line in txt:   
            phrase += line
        phrase = phrase.replace("\n", " ")          
        print(phrase)

#Easier solution / Website's solution 
with open("sample.txt", "r") as file:
    data = file.read().replace("\n", " ")
    print("data")
