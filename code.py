#EMOJI CONVERTER
#simple emoji converter in python
#you can find corresponding smily faces according to your input
#you can get smily faces by pressing "windows+dot" in Windows Operating System

#dictionary containing emojis and their smily face
emojis={
    ":)":"π",
    ":(":"π",
    "xD":"π",
    "-_-":"π",
    "00":"π",
    "*-*":"π€©",  
    ";)":"π",
    ";(":"πͺ",
    "^^":"π",
}

#input from user of smily face/emoji
emojisymbol=input("Enter Emoji 'like :)': ")
if emojisymbol in emojis:
    print('Smily Face corresponding to Your Emoji is:',emojis[emojisymbol])
else:
    print('π ps Sorryπ')
    print(emojisymbol,'is not defined in Emoji Dictionary')
