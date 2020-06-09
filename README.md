![loopyng logo](https://user-images.githubusercontent.com/62253156/82760979-3d40da80-9dc5-11ea-8690-652f656f565f.png)

<h2>Um programa escrito em python que tem como objetivo replicar uma loop station gravando e reproduzindo em loopping seu microfone.</h2>

<br/>
	
	
### :thinking: O que é uma loop station? 
segue um vídeo exemplo: https://www.youtube.com/watch?v=Zdrx3YS9v8k


### :keyboard: Um pouco mais sobreo projeto: (vídeo em desenvolvimento)



## 	:arrow_forward: Uso:
Iicialize o arquivo **Tk_main.py** com algum interpretador python, o programa ja estará funcionando. A interface grafica
te ajudará a saber o que esta acontecendo. Para resumir: aperte uma das letrar **A, S, D** ou **F** para gravar um audio, 
cada uma delas representa um dos pedais da loop station e cada uma suporta gravar uma faixa de som. Assim que quiser
parar a gravação basta apertar espaço e o audio que fora gravado se repetira até o fechamento do programa. 

Após a gravação do primeiro pedal (letra) é possível gravar nos outros e assim por diante. ainda existem funcionalidade
a serem implementadas e também existe um possível **bug** (na versão de terminal) onde seu audio fica estourado, é apenas reiniciar o computador que tudo voltará ao normal.


 <h3> Se divirta! <h3/>


# :newspaper:Layout
![layout](https://user-images.githubusercontent.com/62253156/83658080-b7c0e580-a58f-11ea-8843-82264b3d77b1.png)


## 	:globe_with_meridians:	 Tecnologias:
- Gravação de audio
- Criação e reprodução de arquivos .wav
- threading para uso de multiplas funções simultaneamente
- Keybord listener para receber comandos do teclado.
- TKinter para inteface gráfica
- webbrowser para redirecionar para o navegador


## :blue_book: Bibliotecas:

> keyboard

> playsound

> wave

> pyaudio

> threading

> pilow

> tk inter

> webbrowser
 

### :warning: Bugs: :warning:
> todos os bugs estão sendo arrumados
- Necessário reiniciar o programa para usa-lo novamente.

- Não existe (ainda) sistema de play e pause dos audios gravados.


### :crystal_ball: Implementações futuras
- Interface gráfica
    * sliders para controle de volume
- Um sistema de play e pause dos áudios que já estão tocando
- grafico do microfone em tempo real (usando pyaudio)
- botão para ativar metronomo + area de texto para mudar o seu ritimo
- Mais pedais de gravação
- Uma melhora no som que é gravado, tanto no quesito musical quanto de qualidade de som
- suporte para instrumentos via cabo
