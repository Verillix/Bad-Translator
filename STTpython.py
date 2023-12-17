#import library
from googletrans import Translator
from PyMultiDictionary import MultiDictionary
import speech_recognition as sr
import Caribe as cb


# Initialize recognizer class (for recognizing the speech)
dictionary = MultiDictionary()
translator= Translator()
r = sr.Recognizer()
languages = ['bengali','bn','german','de','english','en','spanish','es','French','fr','hindi','hi','italian','it','japanese','ja','javanese','jv','korean','ko','malay','ms','marathi','mr','polish','pl','portugese','pt','romanian','ro','russian','ru','tamil','ta','turkish','tr','ukrainian','uk','chinese','zh']
possibleLanguages = []
possibleLanguages2 = []
correctLanguage = ""

def detectSpokenLang():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    languageT = 1
    for i in range(int(len(languages)/2)):
        try:
            speechText = (str(r.recognize_google(audio_text, language = languages[languageT])))
            print(speechText)
            possibleLanguages.append(languages[languageT])
            languageT = languageT + 2
        except:
            languageT = languageT + 2
    print(possibleLanguages)
    for i in range(len(possibleLanguages)):
        speechText2 = (str(r.recognize_google(audio_text, language = possibleLanguages[i])))
        translation = translator.translate(speechText2).text
        correction = (cb.caribe_corrector(translation))
        correction = correction[:(len(correction)-1)]
        if translation == correction:
            possibleLanguages2.append(possibleLanguages[i])
    print(possibleLanguages2)
    for i in range(len(possibleLanguages2)):
        for j in range(len(translation.split())):
            try:
                dictionary.meaning(possibleLanguages[1],translation.split()[i])
            except:
                possibleLanguages2.remove(possibleLanguages2[i])
    correctLanguage = possibleLanguages2[0] 
    print(correctLanguage)
    correctText = str(r.recognize_google(audio_text, language = correctLanguage))
    try:
        spoken = languages.index(correctLanguage)-1
        pyscript.write("The language is: ",languages[spoken])
        pyscript.write("Text: ", correctText)
        translated = translator.translate(correctText).text
        pyscript.write("Translated Text: ", translated)
    except:
        pyscript.write("Sorry, I did not get that")
    return()
def detectTextLang():
    languages[17] = 'jw'
    languages[39] = 'zh-cn'
    languageT = 1
    Text = input("text: ")
    translation = translator.translate(Text)
    correctLanguage = translation.src
    typed = languages.index(correctLanguage) -1
    print("The language is:",languages[typed])
    print("Text: ",Text)
    print("Translation: ",translation.text)
    return()
