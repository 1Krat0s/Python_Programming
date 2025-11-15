from nicegui import ui

# h = 0x9E3779B1
# characters = input()
# for i in range(len(characters)):
#    c = characters[i]
 #   h = h ^ ord(c)
  #  h = h * 0x517CC1C7
   # h = h & 0xFFFFFFFF
#h = h ^ len(characters)
#print(h)

def hashing(input_string):
    h = 0x9E3779B1
    characters = input_string
    for i in range(len(characters)):
        c = characters[i]
        h = h ^ ord(c)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
    h = h ^ len(characters)
    return h

input_field = None
hash_label = None

def update_hash():
    text_to_hash = input_field.value
    final_hash = hashing(text_to_hash)
    hash_label.set_text(f"Hash value: {final_hash}")


with ui.card().classes('w-96 p-4 shadow-xl'):
    ui.label("Hashing").classes('text-h5 text-green-700 font-bold') 
    ui.separator()
    input_field = ui.input(label= "Enter Message to Hash", placeholder= "Type here...").classes('w-full')
    initial_hash = hashing(input_field.value)
    hash_label = ui.label(f"Hash value: {initial_hash}").classes('text-lg font-mono q-pa-sm bg-yellow-100 rounded')
    ui.button("GET HASH", on_click= update_hash, color= "blue").classes('mt-4')

ui.run(title= "HW7_GUI")