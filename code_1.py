import pyfiglet

def text_to_ascii_art(text, font="standard"):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except pyfiglet.FontNotFound:
        print(f"Font '{font}' not found. Using standard font instead.")
        ascii_art = pyfiglet.figlet_format(text)
        return ascii_art

text = input("Enter text to convert : ")
font = input("Enter font (press Enter for standard): ")
ascii_art = text_to_ascii_art(text, font)
print(ascii_art)
