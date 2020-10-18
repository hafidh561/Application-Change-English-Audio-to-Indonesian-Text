from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from ibm_watson import SpeechToTextV1


def main():
	# API KEY Convert Suara ke Text
	url_s2t = "YOUR URL KEY"
	iam_apikey_s2t = "YOUR API KEY"

	# API Key Translate Bahasa
	url_lt = 'YOUR URL KEY'
	apikey_lt = 'YOUR API KEY'
	version_lt = '2018-05-01'

	print("Program Translate Audio English ke Text Indonesia\n")

	# Program Convert Suara ke Text
	authenticator = IAMAuthenticator(iam_apikey_s2t)
	s2t = SpeechToTextV1(authenticator=authenticator)
	s2t.set_service_url(url_s2t)
	filename = input("Masukkan nama file: ")
	with open(filename, mode="rb") as wav:
		if filename is None:
			raise FileNotFoundError()
		print("\nHarap tunggu ya")
		response = s2t.recognize(audio=wav, content_type='audio/mp3')
	hasil = response.result["results"]
	sounds = list()
	for suara in hasil:
		sounds.append(suara["alternatives"][0]["transcript"])

	# Program Translate Bahasa
	authenticator = IAMAuthenticator(apikey_lt)
	language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
	language_translator.set_service_url(url_lt)
	with open("hasil (" + filename + ").txt", "w") as file:
		print("\nBanyak doa gan biar cepet")
		for sound in sounds:
			translation_response = language_translator.translate(text=sound, model_id='en-id')
			translation = translation_response.get_result()
			file.write(translation["translations"][0]["translation"] + "\n")
	print("\nProgram selesai")


if __name__ == "__main__":
	main()
