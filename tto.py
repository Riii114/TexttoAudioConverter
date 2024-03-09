# from gtts import gTTS
# import os
# import gtts

# def text_to_audio(text, language='en', gender='male'):
#     if gender.lower() == 'male':
#         if language.lower() == 'en':
#             language_code = 'en-US'
#             voice = 'en-US-Male'
#         elif language.lower() == 'fr':
#             language_code = 'fr-fr'
#             voice = 'fr-fr'
#         # Add more languages and their corresponding voices as needed
#         else:
#             print("Invalid language option. Using English.")
#             language_code = 'en-US'
#             voice = 'en-US-Male'
            
#     elif gender.lower() == 'female':
#         if language.lower() == 'en':
#             language_code = 'en-us'
#             voice = 'en-us-female'
#         elif language.lower() == 'fr':
#             language_code = 'fr-fr'
#             voice = 'fr-fr-wavenet-b'
#         # Add more languages and their corresponding voices as needed
#         else:
#             print("Invalid language option. Using English.")
#             language_code = 'en-us'
#             voice = 'en-US-female'
#     else:
#         print("Invalid gender option. Using male voice.")
#         language_code = 'en-us'
#         voice = 'en-US-Male'
    
#     #Check if the specified voice is available:
#     tts = gtts.gTTS(text=text,lang=language_code)    

#     #Detect if the selected voice is a male voice
#     male_voices = {'en-US':['en-US-Male'],'fr-fr':['fr-fr'], 'es-ES': ['es-ES-Male'], 'de-DE': ['de-DE-Male']} #Add more languages and their corresponding male voices as needed
#     if voice not in male_voices.get(language_code,[['en-US-Male']]):
#         print("warning : The selected voice is not a male voice.")

#     tts = gTTS(text=text, lang=language_code, slow=False)
#     tts.save("output.mp3")
#     os.system("start output.mp3")  # This will open the audio file with the default system player

# if __name__ == "__main__":
#     text = input("Enter the text to convert to audio: ")
#     language = input("Enter the language (e.g., en for English, fr for French): ")
#     gender = input("Enter the gender (male/female): ")
#     text_to_audio(text, language, gender)

from gtts import gTTS
import os

def text_to_audio(text, language='en', voice='male'):
    if voice.lower() == 'male':
        if language.lower() == 'en':
            language_code = 'en-US'
            voice_name = 'en-US-Male'
        elif language.lower() == 'fr':
            language_code = 'fr-fr'
            voice_name = 'fr-FR-Wavenet-A'
        # Add more languages and their corresponding male voices as needed
        else:
            print("Invalid language option. Using English.")
            language_code = 'en-US'
            voice_name = 'en-US-Male'

    elif voice.lower() == 'female':
        if language.lower() == 'en':
            language_code = 'en-US'
            voice_name = 'en-US-Wavenet-C'
        elif language.lower() == 'fr':
            language_code = 'fr-fr'
            voice_name = 'fr-FR-Wavenet-B'
        # Add more languages and their corresponding female voices as needed
        else:
            print("Invalid language option. Using English.")
            language_code = 'en-US'
            voice_name = 'en-US-Wavenet-C'
    else:
        print("Invalid voice option. Using male voice.")
        language_code = 'en-US'
        voice_name = 'en-US-Male'

    tts = gTTS(text=text, lang=language_code, tld='com', slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # This will open the audio file with the default system player

if __name__ == "__main__":
    text = input("Enter the text to convert to audio: ")
    language = input("Enter the language (e.g., en for English, fr for French): ")
    voice = input("Enter the voice (male/female): ")
    text_to_audio(text, language, voice)