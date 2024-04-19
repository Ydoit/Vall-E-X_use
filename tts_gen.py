import sys
sys.path.append("/home/ydoit/AIGC/Vall-E-X/VALL-E-X")
sys.path.append("/home/ydoit/AIGC/Vall-E-X/VALL-E-X/Vallutils")

from generation import SAMPLE_RATE, generate_audio, preload_models
from prompt_making import make_prompt
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
import os
# download and load all models
preload_models()

# # generate audio from text
# text_prompt = """
# Hello, my name is Nose. And uh, and I like hamburger. Hahaha... But I also have other interests such as playing tactic toast.
# """
# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav("vallex_generation.wav", SAMPLE_RATE, audio_array)

# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)
# zh_speaker_path="/home/ydoit/AIGC/Raw-ZH/Vall-e-x/zh"
# count=0
# for row in os.listdir(zh_speaker_path):
#     make_prompt(name=f"zh-speaker{count+1}", audio_prompt_path=f"{zh_speaker_path}/{row}")
#     count+=1
#     if count>=10:
#         break
# en_speaker_path="/home/ydoit/AIGC/Raw-EN/Vall-e-x/en"
# count=0
# for row in os.listdir(en_speaker_path):
#     make_prompt(name=f"en-speaker{count+1}", audio_prompt_path=f"{en_speaker_path}/{row}")
#     count+=1
#     if count>=10:
#         break
with open ('zh-text.txt','r',encoding='utf-8') as f:
    zh=f.readlines()
    count=0
    for row in zh:
        i=int(count/10)
        j=int(count%10)
        audio=generate_audio(row,language='zh',prompt=f"zh-speaker{i+1}")
        write_wav(f"output/zh/speaker{i+1}/audio{j+1}.wav",SAMPLE_RATE,audio)
        with open (f"output/zh/speaker{i+1}/audio{j+1}.txt",'w',encoding='utf-8') as f:
            f.write(row)
        count+=1
with open('en-text.txt','r',encoding='utf-8') as f:
    en=f.readlines()
    count=0
    for row in en:
        i=int(count/10)
        j=int(count%10)
        audio=generate_audio(row,language='en',prompt=f"en-speaker{i+1}")
        write_wav(f"output/en/speaker{i+1}/audio{j+1}.wav",SAMPLE_RATE,audio)
        with open (f"output/en/speaker{i+1}/audio{j+1}.txt",'w',encoding='utf-8') as f:
            f.write(row)
        count+=1
        