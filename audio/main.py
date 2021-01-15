#  import mp3play
from playsound import playsound
# import vlc
# import time
import os


def get_project_path():
    return os.getcwd()
    # return os.getenv('BOIL_CTRL_ROOT')

def get_dir_path(dirname):
    return os.path.join(get_project_path(), dirname)

def main():
    # with open(get_dir_path('code/code0.mp3'), 'r', encoding='utf-8') as f:
    #     p = vlc.MediaPlayer(f)
    #     p.play()

    # with open(get_dir_path('audio/code/code0.mp3'), 'r') as f:
    #     playsound(f)
    print('start')
    playsound(get_dir_path('audio/code/code0.mp3'))
    print('end')

    # clip = None
    # with open(get_dir_path('code/code0.mp3'), 'r', encoding='utf-8') as f:
    #     clip = mp3play.load(f)
    # if clip is None:
    #     return
    # clip.play()
    # time.sleep(min(30, clip.seconds()))
    # clip.stop()

if __name__ == "__main__":
    main()
