import os
import time
from gtts import gTTS
from moviepy.editor import VideoFileClip, concatenate_videoclips

'''

Used for testing and debbuging

'''


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

def handle_files():

   files = []
   while 1:
      # add the files in the test directory to the list only if they end in .txt
      # if the file is not in the list, add it

      for file in os.listdir('teste'):
         if file.endswith('.txt') and file not in files:
            files.append(file)
            print(f'Arquivo {file} adicionado à lista\n')

      print(files)

      time.sleep(3)

   return

def shuffle_videos():
   # shuffle the video files from the interviewer folder with the respostas_texto folder

   # get the list of files from the interviewer folder
   interviewer_files = os.listdir('videos_entrevistador')

   # get the list of files from the respostas_texto folder
   respostas_files = os.listdir('respostas_audio')

   # create a list that add one file from the interviewer then one file from the respostas_texto
   # until the end of the list alternating between the two folders
   shuffled_files = []
   for i in range(len(interviewer_files)):
      shuffled_files.extend([interviewer_files[i], respostas_files[i]])

   print(shuffled_files)
   return

if __name__ == "__main__":
   pass
   #shuffle_videos()
   #generate_text_to_speech()
