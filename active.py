from pygame import mixer 
from datetime import datetime
import time
def send_to_file(audio):
    with open(f'{audio}.txt','a') as text:
        text.write(f'{time.asctime()}\n')


def play_audio(audio):
    mixer.init() 
    mixer.music.load(f"{audio}.mp3") 
    mixer.music.set_volume(60) 
    mixer.set_num_channels(100)
    mixer.music.play(-1) 
    # infinite loop 
    while True: 
        
        print("Press 'p' to pause, 'r' to resume") 
        print("Press 'done' to exit the program") 
        query = input() 
        
        if query == 'p': 
    
            # Pausing the music 
            mixer.music.pause()      
        elif query == 'r': 
    
            # Resuming the music 
            mixer.music.unpause() 
        elif query == 'done': 
    
            # Stop the mixer 
            mixer.music.stop() 
            send_to_file(audio)
            break

def run_timer(now):
    while(time.localtime().tm_hour<18):
        later=time.time()
        lap=round(later-now)
        print(lap)
        time.sleep(1)
        if(lap%3600==0):
            print('drink water')
            play_audio('water')
        if(lap%1800==0):
            print('for eyes')
            play_audio('eyes')
        if(lap%2700==0):
            print('exercise')
            play_audio('exercise')




def start_timer():
    today=datetime(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,9,0,0)
    today=datetime.timestamp(today)

    while(True):
        if (time.time()>=today):
            print('running')
            run_timer(today)
            break
start_timer()