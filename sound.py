import pygame
import os

# Initialize pygame
pygame.mixer.init()

# Replace 'sound_files' with a list of sound file paths you want to play
sound_files = ['y2mate.com - Don Williams  Best Of Songs Don Williams  Don Williams Greatest Hits Full Album HD.mp3', 'Mercy-Chinwo-Kosi-(TrendyBeatz.com) (1).mp3', 'Right-Said-Fred-Stand-Up-For-The-Champions-Wiseloaded-com.mp3']
current_sound_index = 0

def play_sound():
    pygame.mixer.music.load(sound_files[current_sound_index])
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

def pause_play_sound():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def next_sound():
    global current_sound_index
    stop_sound()
    current_sound_index = (current_sound_index + 1) % len(sound_files)
    play_sound()

def previous_sound():
    global current_sound_index
    stop_sound()
    current_sound_index = (current_sound_index - 1) % len(sound_files)
    play_sound()

# Initialize pygame for handling keyboard events
pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause_play_sound()
            elif event.key == pygame.K_RIGHT:
                next_sound()
            elif event.key == pygame.K_LEFT:
                previous_sound()
        if event.type == pygame.QUIT:
            stop_sound()
            pygame.quit()
            quit()
