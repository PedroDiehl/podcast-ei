import os
from gtts import gTTS

def save_speech(text: str, file_number: int):
   language = 'pt-br'
   speech = gTTS(text=text, lang=language, slow=False)
   speech.save(f'respostas_audio/{file_number}.wav')

def generate_text_to_speech():
   print()

   for file_number in range(1, 11):
      print(f'Gerando áudio para o arquivo {file_number}.txt')

      with open(f'respostas_texto/{file_number}.txt', 'r', encoding="utf-8") as file:
         text = file.read()
         save_speech(text, file_number)

      print(f'Áudio para o arquivo {file_number}.txt gerado com sucesso!\n')

   return

def list_videos():
   print('Vídeos disponíveis:')

   # list by comprehension
   [print(file) for file in os.listdir('videos_entrevistador') if file.endswith('.mp4')]

   return

if __name__ == "__main__":
   list_videos()
   #generate_text_to_speech()
