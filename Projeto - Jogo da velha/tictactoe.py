import tkinter #tk-interface (Biblioteca de Interface Gráfica do Usuário)

def set_tile(row, column):
    global curr_player

    if(game_over):
        return
    
    if board[row][column]["text"] != "":
        #checa se o local já foi marcado
        return

    board[row][column]["text"] = curr_player #marca o local

    if curr_player == playerO: #muda de jogador
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+"'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns += 1
    
    #horizontal, checa 3 linhas
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != ""):
            label.config(text=board[row][0]["text"] + "'s is the winner!", foreground=color_purple)
            
            for column in range(3):
                board[row][column].config(foreground=color_purple, background=color_lavander)
            
            game_over = True
            return
    
    #vertical, checa 3 linhas
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + "'s is the winner", foreground=color_purple)
            
            for row in range(3):
                board[row][column].config(foreground=color_purple, background=color_lavander)
            
            game_over = True
            return
        
    #diagonal
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + "'s the winner", foreground=color_purple)

        for i in range(3):
            board[i][i].config(foreground=color_purple, background=color_lavander)
        
        game_over = True
        return
    
    #anti-diagonal
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + "'s the winner", foreground=color_purple)
        board[0][2].config(foreground=color_purple, background=color_lavander)
        board[1][1].config(foreground=color_purple, background=color_lavander)
        board[2][0].config(foreground=color_purple, background=color_lavander)

        game_over = True
        return
    
    #empate
    if (turns == 9):
        game_over = True
        label.config(text = "Tie!", foreground=color_purple)

def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=curr_player + "'s turn", foreground=color_pink)

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

#setup do jogo
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0,0,0],[0,0,0],[0,0,0]]

color_blue ="#ADCFD1" 
color_purple = "#BCA0FF" 
color_gray = "#D8E0E9"
color_lavander = "#DACBFF"
color_pink = "#E9A8B2"

turns = 0
game_over = False

#setup da janela
window = tkinter.Tk() #cria a janela do jogo
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 25), background=color_gray, foreground=color_pink)

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_gray, foreground=color_blue, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 25), background=color_gray, foreground=color_pink, command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()


window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)" - Faz com que a janela sempre seja centralizada em relação ao tamanho da tela
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()