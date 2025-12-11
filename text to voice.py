import pyttsx3
# pip install pyttsx3

engine = pyttsx3.init()

text = input("Write the text: ")
engine.save_to_file(text, "voice_output.mp3")
engine.runAndWait()

print("The audio file was created 💤")
