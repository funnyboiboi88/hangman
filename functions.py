#recieve input of word to be used
#prompt user for letter, check letter and respond appropriately


def get_word():
    letterCap = 10
    try:
        word = input("What is your chosen word").upper()
        
        if not word.isalpha():
            raise ValueError("Invalid Word. No special characters, spaces or numbers.")
        
        if len(word) > letterCap:
            raise ValueError("Max letter cap of 10 reached.")
            
    except ValueError as e:
        print("Error:", e)
        
    