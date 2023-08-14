with open(r"C:\Users\ahhes\Documents\GitHub\bookbot\books\frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    chars = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                if chars.get(letter.lower()) == None:
                    chars[letter.lower()] = 0
                chars[letter.lower()] += 1
    print("-- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    sorted_chars = sorted(chars.items(), key= lambda x : x[0])
    for key, value in sorted_chars:
        print(f"The {key} character was found {value} times")
    print("--- End report ---")

        
    
    
    



