![loopyng logo](https://user-images.githubusercontent.com/62253156/82760979-3d40da80-9dc5-11ea-8690-652f656f565f.png)

<h2>A program written in python that aims to replicate a loop station by recording and looping your microphone.</h2>

<br/>
	
	
### :thinking: What is a Loop Station? 
Here is a video explaning: https://www.youtube.com/watch?v=Zdrx3YS9v8k


### :keyboard: Video about the development (in Portuguese): [![Sobre o Projeto - Loopyng](https://res.cloudinary.com/marcomontalbano/image/upload/v1593005006/video_to_markdown/images/youtube--MOxTDfwdxCw-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=MOxTDfwdxCw&t=614s "Sobre o Projeto - Loopyng")



## 	:arrow_forward: Uso:
Initialize the tile ** Tk_main.py **  with some python interpreter, the program will already be working. The graphical interface
will help you to know what is happening. To summarize: press one of the letters ** A, S, D ** or ** F ** to record an audio,
each represents one of the pedals on the loop station and each supports recording a sound track. As soon as you want
stop recording just press space and the audio that was recorded will be repeated until the program closes.

After recording the first pedal (letter) it is possible to record on the others and so on. functionality still exists
to be implemented and there is also a possible ** bug ** (in the terminal version) where your audio is burst, just restart the computer and everything will be back to normal.

 <h3> Have Fun!<h3/>


# :newspaper:Layout
![layout](https://user-images.githubusercontent.com/62253156/83658080-b7c0e580-a58f-11ea-8843-82264b3d77b1.png)


## 	:globe_with_meridians:	 Tecnologies:
- Audio recording
- creation and reproduction of .wav files
- threading for multiple functions simultaneously
- Keybord listener to recebe commands.
- TKinter for graphic interface
- Webbrowser to redirect to chrome page

## :blue_book: Libraries:

> keyboard

> playsound

> wave

> pyaudio

> threading

> pilow

> tk inter

> webbrowser
 

### :warning: Bugs: :warning:
- Need to restar the program to re-use it.

- Doesn't exist a play/pause system.


### :crystal_ball: Future implefmentations
- Graphic Interface
    * Volume Controllers
- Play and pause system
- microphone power graphic
- Metronome system
- Improve recorded sound quality
