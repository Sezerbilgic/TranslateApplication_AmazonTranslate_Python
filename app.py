import boto3
from tkinter import *
from tkinter import ttk, messagebox


root = Tk()
root.geometry("850x300")

def translateFonc():
    for key,value in languageOptions.items():
        if(value == original_combo.get()):
            from_language_key = key

    for key,value in languageOptions.items():
        if(value == translated_combo.get()):
            to_language_key = key


    translated_text.delete(1.0, END)
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

    result = translate.translate_text(Text=original_text.get(1.0, END), SourceLanguageCode=from_language_key, TargetLanguageCode=to_language_key)

    translated_text.insert(1.0, result.get('TranslatedText'))


languageOptions = {
    "en": "English",
    "tr": "Turkish",
    "de": "German",
    "es": "Spanish",
    "ja": "Japanese",
    "zh": "Chinese"
}


languageList = ["English","Turkish","German","Spanish","Japanese","Chinese"]
    

original_text = Text(root, height=10, width=40)
original_text.grid(row=0,column=0, pady=20, padx=10)

translate_button = Button(root, text="Çevir", font=("Helvetica",24), command=translateFonc)
translate_button.grid(row=0,column=1,padx=10)


translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0,column=2, pady=20, padx=10)

original_combo = ttk.Combobox(root,width=50, value=languageList)
original_combo.grid(row=1,column=0)

translated_combo = ttk.Combobox(root,width=50, value=languageList)
translated_combo.grid(row=1,column=2)


root.mainloop()
