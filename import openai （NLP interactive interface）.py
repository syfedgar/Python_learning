import openai
import speech_recognition as sr
import pyttsx3

# 设置OpenAI API密钥
openai.api_key = 'your-api-key'

# 初始化语音识别和合成引擎
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

def respond(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

while True:
    user_input = listen()
    if user_input:
        gpt_response = chat_with_gpt(user_input)
        print(f"ChatGPT: {gpt_response}")
        respond(gpt_response)
