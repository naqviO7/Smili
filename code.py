#EMOJI CONVERTER
#simple emoji converter in python
#you can find corresponding smily faces according to your input
#you can get smily faces by pressing "windows+dot" in Windows Operating System

#dictionary containing emojis and their smily face
emojis={
    ":)":"😊",
    ":(":"😒",
    "xD":"😂",
    "-_-":"😑",
    "00":"👀",
    "*-*":"🤩",  
    ";)":"😅",
    ";(":"😪",
    "^^":"😍",
}

#input from user of smily face/emoji
emojisymbol=input("Enter Emoji 'like :)': ")
if emojisymbol in emojis:
    print('Smily Face corresponding to Your Emoji is:',emojis[emojisymbol])
else:
    print('👀 ps Sorry😕')
    print(emojisymbol,'is not defined in Emoji Dictionary')
