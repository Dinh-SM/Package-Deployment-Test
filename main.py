import sys
from textblob import TextBlob
from googletrans import Translator, constants


def hello_guys(text):
	"""Returns a sympathetic greeting in the language of the given text

	Initializes a translator (form Google Translator API), then detects the given
	text language with TextBlob and finally returns a sympathetic greeting in
	the corresponding language

	Args:
		text (str): given text in a specific language.

	Returns:
		sympathetic_greeting (str): the sympathetic greeting in the corresponding
		language.
	"""
	translator = Translator()

	if text:
		text_blob = TextBlob(text)
		lang = text_blob.detect_language()
		if lang != "en":
			translation = translator.translate("Hello guys!", src="en", dest=lang)
			sympathetic_greeting = translation.text
		else:
			sympathetic_greeting = "Hello guys!"
	else:
		sympathetic_greeting = "No text but hello guys!"

	return sympathetic_greeting

def main():
	if len(sys.argv) > 1:
		result = hello_guys(sys.argv[1])
	else:
		result = hello_guys(None)

	print(result)

if __name__ == '__main__':
	main()