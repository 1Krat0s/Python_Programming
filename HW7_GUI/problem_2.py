from nicegui import ui
import random

MATCH_SOUND = ui.audio('https://nicegui.io/sounds/match.mp3').classes('hidden')
FLIP_SOUND = ui.audio('https://nicegui.io/sounds/flip.mp3').classes('hidden')
WIN_SOUND = ui.audio('https://nicegui.io/sounds/win.mp3').classes('hidden')

CARD_BACK = '❓'
UNIQUE_EMOJIS = ['😊', '😎', '🥳', '🚀', '💡', '🤖', '👑', '🎸']
EMOJIS = []

buttons = []
opened = []
matched = []
move_count = 0
move_label = None

def setup_game():
    global EMOJIS, move_count, buttons, opened, matched
    
    opened.clear()
    matched.clear()
    move_count = 0
    if move_label:
        move_label.set_text(f'Moves: {move_count}')

    EMOJIS = UNIQUE_EMOJIS * 2
    random.shuffle(EMOJIS)
    
    for i, button in enumerate(buttons):
        button.text = CARD_BACK
        button.set_enabled(True) 

def check_win():
    """Checks for the win condition and handles win state."""
    if len(matched) == len(EMOJIS):
        WIN_SOUND.play()
        ui.notify('🎉 You win! All pairs found! 🎉', type='positive', position='center', timeout=5000)
        for button in buttons:
            button.set_enabled(False)

def update_moves():
    global move_count
    move_count += 1
    move_label.set_text(f'Moves: {move_count}')

def reset_pair(i, j):
    buttons[i].text = CARD_BACK
    buttons[j].text = CARD_BACK
    
    opened.clear()

def handle_click(idx):
    if idx in matched or idx in opened or len(opened) >= 2:
        return

    FLIP_SOUND.play()

    buttons[idx].text = EMOJIS[idx]
    opened.append(idx)

    if len(opened) == 2:
        update_moves()
        i, j = opened
        
        if EMOJIS[i] == EMOJIS[j]:
            MATCH_SOUND.play()
            matched.extend([i, j])
            opened.clear()
            check_win()
        else:
            ui.timer(0.5, lambda: reset_pair(i, j), once=True)

ui.query('.q-page').classes('flex justify-center items-center')

with ui.card().classes('p-6 shadow-xl w-fit'):
    ui.label('Memory Game').classes('text-h4 q-py-md text-blue-800 text-center w-full')

    with ui.row().classes('w-full justify-around items-center'):
        move_label = ui.label(f'Moves: 0').classes('text-lg font-bold')
        
        ui.button('RESTART', on_click=setup_game, icon='refresh', color='red')
    
    ui.separator()

    with ui.grid(columns=4).classes('gap-2'):
        for i in range(16):
            button = ui.button(text= CARD_BACK, on_click= lambda i= i: handle_click(i)).classes('w-16 h-16 text-2xl bg-blue-500 hover:bg-blue-600')
            buttons.append(button)

setup_game() 

ui.run(title='Memory Game')