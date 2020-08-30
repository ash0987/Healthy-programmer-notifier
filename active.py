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

def run_timer(intial):
    intial_water=intial
    intial_eye=intial
    intial_phy=intial
    while(True):
        print('running')
        later=time.time()

        if(later-intial_water>=3600):
            print('drink water')
            play_audio('water')
            intial_water=time.time()
        if(later-intial_eye>=1800):
            print('for eyes')
            play_audio('eyes')
            intial_eye=time.time()
        if(later-intial_phy>=2700):
            print('exercise')
            play_audio('exercise')
            intial_phy=time.time()
        time.sleep(1)




def start_timer():
    intial=time.time()
    
    run_timer(intial)
    
start_timer()