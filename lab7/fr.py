import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "musics"
music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
music_files.sort()  
current_track = 0  

def play_music():
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, music_files[current_track]))
    pygame.mixer.music.play()

if music_files:
    play_music()
else:
    print("No MP3 files found in the 'musics' folder.")
    exit()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    play_music()

            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()

            elif event.key == pygame.K_n: 
                current_track = (current_track + 1) % len(music_files)
                play_music()

            elif event.key == pygame.K_p:  
                current_track = (current_track - 1) % len(music_files)
                play_music()

pygame.quit()