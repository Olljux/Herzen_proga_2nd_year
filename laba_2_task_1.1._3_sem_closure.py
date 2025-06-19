def about_me():
    name = 'Olya'
    surname = 'Ivanova'
    birthday = '30.07.2004'
    zodiac_sign = 'Leo'
    
    def meet():
        print(f"My name is {name} {surname}, i was born {birthday}, my zodiac is {zodiac_sign}.")
    return meet

x = about_me()
x()