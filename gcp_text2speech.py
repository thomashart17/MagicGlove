import os
from google.cloud import texttospeech # outdated or incomplete comparing to v1
from google.cloud import texttospeech_v1

def speech_to_text(colour, audio_file_path):
    print("Running GCP...")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"path to json"

    # Instantiates a client
    client = texttospeech_v1.TextToSpeechClient()
    
    # Set the text input to be synthesized
    colour_phrase = f"The colour is {colour}"
    synthesis_input = texttospeech_v1.SynthesisInput(text=colour_phrase)


    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-ca", 
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(audio_file_path, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "audiofile.mp3"')
    
