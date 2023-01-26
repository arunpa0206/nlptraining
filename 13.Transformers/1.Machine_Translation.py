from transformers import pipeline

translation = pipeline("translation_en_to_de")
text = "I was Walking"
translated_text = translation(text, max_length=40)[0]['translation_text']
print("Translated text : {}".format(translated_text))
