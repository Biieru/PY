import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Listagem dos decks
decks = [
   {"Deck": "Trickstar", "Personagem": "Blue Angel", "Skill": "Holy Angel Trick", "Tipo": "Burn", "Consistência": 7.0, "Diversão": 7.5, "Ofensiva": 4.0, "Defensiva": 4.0},
    {"Deck": "Ritual Beast", "Personagem": "Marik", "Skill": "Shadow Game", "Tipo": "Stall Burn", "Consistência": 10.0, "Diversão": 10.0, "Ofensiva": 6.0, "Defensiva": 8.0},
    {"Deck": "Blue Luster", "Personagem": "Yugizinho", "Skill": "Battle Chronicle", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 6.0, "Ofensiva": 8.0, "Defensiva": 5.0},
    {"Deck": "Deckout!", "Personagem": "Tea", "Skill": "Duel, Standby!", "Tipo": "Deckout", "Consistência": 5.0, "Diversão": 9.0, "Ofensiva": 3.0, "Defensiva": 7.0},
    {"Deck": "Harpy Time", "Personagem": "Mai", "Skill": "Harpie's Hunting Ground", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 7.0, "Ofensiva": 7.0, "Defensiva": 4.0},
    {"Deck": "Buster Blader", "Personagem": "Yami Yugi", "Skill": "Destiny Draw", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 8.0, "Ofensiva": 8.0, "Defensiva": 5.0},
    {"Deck": "Dark Magician", "Personagem": "Yami Yugi", "Skill": "Magician's Magic", "Tipo": "Controle", "Consistência": 7.5, "Diversão": 7.0, "Ofensiva": 7.0, "Defensiva": 6.0},
    {"Deck": "Thousand-Eyes Illusion", "Personagem": "Pegasus", "Skill": "Thousand-Eyes Illusion", "Tipo": "Stall Controle", "Consistência": 7.0, "Diversão": 9.0, "Ofensiva": 3.0, "Defensiva": 8.0},
    {"Deck": "Aromagico", "Personagem": "Pegasus", "Skill": "Mind Scan", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 7.0, "Ofensiva": 5.0, "Defensiva": 8.0},
    {"Deck": "Draw Burn", "Personagem": "Orion", "Skill": "Chain Reaction", "Tipo": "Burn", "Consistência": 6.5, "Diversão": 7.0, "Ofensiva": 3.0, "Defensiva": 5.0},
    {"Deck": "Timelord", "Personagem": "Orion", "Skill": "Chain Reaction", "Tipo": "Burn", "Consistência": 7.0, "Diversão": 8.0, "Ofensiva": 4.0, "Defensiva": 6.5},
    {"Deck": "Paleozoic", "Personagem": "Orion", "Skill": "Chain Reaction", "Tipo": "Stall Burn", "Consistência": 6.5, "Diversão": 8.0, "Ofensiva": 7.0, "Defensiva": 6.5},
    {"Deck": "Cubic", "Personagem": "Aigami", "Skill": "Cubic Seeds", "Tipo": "Stall", "Consistência": 8.0, "Diversão": 9.0, "Ofensiva": 5.0, "Defensiva": 9.0},
    {"Deck": "Greydle Kaiju", "Personagem": "Tea DSOD", "Skill": "Holy Guard", "Tipo": "Stall", "Consistência": 7.5, "Diversão": 8.5, "Ofensiva": 5.0, "Defensiva": 6.5},
    {"Deck": "Magician Girls", "Personagem": "Tea DSOD", "Skill": "Magician Girls", "Tipo": "Controle", "Consistência": 8.0, "Diversão": 7.0, "Ofensiva": 5.0, "Defensiva": 8.5},
    {"Deck": "Predapratico", "Personagem": "Tea DSOD", "Skill": "Holy Guard", "Tipo": "Controle", "Consistência": 6.5, "Diversão": 7.0, "Ofensiva": 7.5, "Defensiva": 4.5},
    {"Deck": "WitchCrafter", "Personagem": "Tea DSOD", "Skill": "Grit", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 7.0, "Ofensiva": 7.0, "Defensiva": 7.0},
    {"Deck": "Blue Eyes", "Personagem": "Kaiba DSOD", "Skill": "Ultimate Dragons", "Tipo": "Aggro", "Consistência": 8.0, "Diversão": 7.0, "Ofensiva": 9.0, "Defensiva": 5.5},
    {"Deck": "LunaLight", "Personagem": "Zane", "Skill": "Fatal Five", "Tipo": "OTK Controle", "Consistência": 6.5, "Diversão": 7.0, "Ofensiva": 8.0, "Defensiva": 6.0},
    {"Deck": "Cyber Angel", "Personagem": "Alexis", "Skill": "Master of Rites II", "Tipo": "Controle", "Consistência": 6.5, "Diversão": 6.5, "Ofensiva": 7.0, "Defensiva": 4.0},
    {"Deck": "Ancient Gear", "Personagem": "Crowler", "Skill": "Battle! Ancient Gear", "Tipo": "Aggro", "Consistência": 7.0, "Diversão": 7.0, "Ofensiva": 9.0, "Defensiva": 3.0},
    {"Deck": "Yubel Neos", "Personagem": "Yubel", "Skill": "Eternal Bond", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 6.5, "Ofensiva": 7.0, "Defensiva": 8.0},
    {"Deck": "Millbel", "Personagem": "Yubel", "Skill": "My Name Is Yubel", "Tipo": "Mill", "Consistência": 8.0, "Diversão": 9.0, "Ofensiva": 2.0, "Defensiva": 8.0},
    {"Deck": "Favorite Hero", "Personagem": "Jaden/Yubel", "Skill": "Favorite Duel", "Tipo": "Controle", "Consistência": 7.0, "Diversão": 7.5, "Ofensiva": 8.0, "Defensiva": 5.0},
    {"Deck": "Volcanic Burn", "Personagem": "Axel", "Skill": "Reloading!", "Tipo": "Burn", "Consistência": 6.0, "Diversão": 9.0, "Ofensiva": 5.0, "Defensiva": 8.5},
    {"Deck": "OTK Gaia", "Personagem": "Supreme King", "Skill": "Dark Fusion", "Tipo": "OTK Aggro", "Consistência": 7.0, "Diversão": 6.5, "Ofensiva": 9.0, "Defensiva": 3.5},
    {"Deck": "Coveiro", "Personagem": "Jaden", "Skill": "Fusion Time!", "Tipo": "Controle", "Consistência": 8.0, "Diversão": 7.0, "Ofensiva": 6.0, "Defensiva": 7.5},
    {"Deck": "Quasar Dragon", "Personagem": "Yusei", "Skill": "A Bond Illuminates the Future", "Tipo": "Controle", "Consistência": 8.0, "Diversão": 7.0, "Ofensiva": 7.5, "Defensiva": 5.5},
    {"Deck": "Mekk Buster Blader", "Personagem": "Aki", "Skill": "Draw Sense: Low-Level", "Tipo": "Controle", "Consistência": 8.5, "Diversão": 8.0, "Ofensiva": 8.0, "Defensiva": 5.5},
    {"Deck": "Timelords", "Personagem": "Z-One", "Skill": "Empy, Infinite and Infinite Light", "Tipo": "Burn ", "Consistência": 9.0, "Diversão": 9.0, "Ofensiva": 7.0, "Defensiva": 7.5},
    {"Deck": "Pobreza Galática", "Personagem": "Kite", "Skill": "XYZ Galaxy", "Tipo": "Aggro", "Consistência": 7.0, "Diversão": 5.5, "Ofensiva": 7.0, "Defensiva": 5.0},
    {"Deck": "Noble Knights", "Personagem": "Kite", "Skill": "Number's Rule", "Tipo": "Controle", "Consistência": 6.0, "Diversão": 6.0, "Ofensiva": 6.5, "Defensiva": 4.5},
    {"Deck": "Railway", "Personagem": "Anna", "Skill": "Unstoppable Train!", "Tipo": "Aggro", "Consistência": 7.5, "Diversão": 6.5, "Ofensiva": 8.5, "Defensiva": 4.5},
    {"Deck": "Golden Castle Of Disney", "Personagem": "Dennis", "Skill": "LP Boost: X4", "Tipo": "Stall", "Consistência": 6.0, "Diversão": 8.5, "Ofensiva": 4.5, "Defensiva": 7.5},
    {"Deck": "Odd-Eyes Rage", "Personagem": "Yuto", "Skill": "Raging Pendulum", "Tipo": "Combo", "Consistência": 7.0, "Diversão": 7.0, "Ofensiva": 8.5, "Defensiva": 4.5},
    {"Deck": "Solfachord", "Personagem": "Zuzu", "Skill": "United Pendulums", "Tipo": "Controle", "Consistência": 6.5, "Diversão": 6.5, "Ofensiva": 6.5, "Defensiva": 6.5},
    {"Deck": "Pesadown", "Personagem": "Gong", "Skill": "HeavyStrong Strategy", "Tipo": "Controle", "Consistência": 8.0, "Diversão": 7.0, "Ofensiva": 5.5, "Defensiva": 8.5},
    {"Deck": "Yosenju", "Personagem": "Sylvio", "Skill": "Neo New Sylvio", "Tipo": "Aggro Controle", "Consistência": 7.5, "Diversão": 7.5, "Ofensiva": 7.5, "Defensiva": 7.5},
    {"Deck": "Fofo", "Personagem": "Sora", "Skill": "The Most Unbearable Monster", "Tipo": "Aggro Controle", "Consistência": 7.5, "Diversão": 6.5, "Ofensiva": 7.5, "Defensiva": 5.5},
    {"Deck": "Amazoness", "Personagem": "Tea DSOD", "Skill": "Holy Guard", "Tipo": "Aggro Controle", "Consistência": 7.5, "Diversão": 7.5, "Ofensiva": 7.5, "Defensiva": 6.5},
    {"Deck": "Gouki", "Personagem": "The Gore", "Skill": "The Main Event: Gouki", "Tipo": "Aggro", "Consistência": 7.0, "Diversão": 6.0, "Ofensiva": 8.0, "Defensiva": 4.0}
        # Adicionar os outros decks sempre seguindo esse formato
]

def pick_random_deck():
    return random.choice(decks)

def pick_deck_by_type(tipo):
    filtered_decks = [deck for deck in decks if tipo.lower() in deck["Tipo"].lower()]
    return random.choice(filtered_decks) if filtered_decks else None

def pick_deck_by_character(personagem):
    filtered_decks = [deck for deck in decks if personagem.lower() == deck["Personagem"].lower()]
    return random.choice(filtered_decks) if filtered_decks else None

def pick_deck_by_rating(criterio, nota):
    filtered_decks = [deck for deck in decks if deck[criterio] >= nota]
    return random.choice(filtered_decks) if filtered_decks else None

def pick_deck_by_average_rating(media):
    filtered_decks = [deck for deck in decks if (deck["Consistência"] + deck["Diversão"] + deck["Ofensiva"] + deck["Defensiva"]) / 4 >= media]
    return random.choice(filtered_decks) if filtered_decks else None

def show_deck(deck):
    messagebox.showinfo("Deck Escolhido", f"""
    Deck: {deck["Deck"]}
    Personagem: {deck["Personagem"]}
    Skill: {deck["Skill"]}
    Tipo: {deck["Tipo"]}
    Consistência: {deck["Consistência"]}
    Diversão: {deck["Diversão"]}
    Ofensiva: {deck["Ofensiva"]}
    Defensiva: {deck["Defensiva"]}
    """)

def show_random_deck():
    deck = pick_random_deck()
    show_deck(deck)

def show_deck_by_type():
    tipo = combo_tipo.get()
    deck = pick_deck_by_type(tipo)
    if deck:
        show_deck(deck)
    else:
        messagebox.showinfo("Aviso", f"Nenhum deck encontrado para o tipo '{tipo}'.")

def show_deck_by_character():
    personagem = combo_personagem.get()
    deck = pick_deck_by_character(personagem)
    if deck:
        show_deck(deck)
    else:
        messagebox.showinfo("Aviso", f"Nenhum deck encontrado para o personagem '{personagem}'.")

def show_deck_by_rating():
    criterio = combo_criterio.get()
    nota = float(entry_nota.get())
    deck = pick_deck_by_rating(criterio, nota)
    if deck:
        show_deck(deck)
    else:
        messagebox.showinfo("Aviso", f"Nenhum deck encontrado com nota maior ou igual a {nota} para o critério '{criterio}'.")

def show_deck_by_average_rating():
    media = float(entry_media.get())
    deck = pick_deck_by_average_rating(media)
    if deck:
        show_deck(deck)
    else:
        messagebox.showinfo("Aviso", f"Nenhum deck encontrado com média geral maior ou igual a {media}.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Deck Picker - Yu-Gi-Oh! Duel Links")

# Criando abas
tab_control = ttk.Notebook(root)
tab_random = ttk.Frame(tab_control)
tab_type = ttk.Frame(tab_control)
tab_character = ttk.Frame(tab_control)
tab_rating = ttk.Frame(tab_control)
tab_avg_rating = ttk.Frame(tab_control)

tab_control.add(tab_random, text='Aleatório')
tab_control.add(tab_type, text='Por Tipo')
tab_control.add(tab_character, text='Por Personagem')
tab_control.add(tab_rating, text='Por Avaliação')
tab_control.add(tab_avg_rating, text='Por Média Geral')
tab_control.pack(expand=1, fill='both')

# Frame para cada aba
frame_random = ttk.Frame(tab_random, padding="20")
frame_random.grid(row=0, column=0)

frame_type = ttk.Frame(tab_type, padding="20")
frame_type.grid(row=0, column=0)

frame_character = ttk.Frame(tab_character, padding="20")
frame_character.grid(row=0, column=0)

frame_rating = ttk.Frame(tab_rating, padding="20")
frame_rating.grid(row=0, column=0)

frame_avg_rating = ttk.Frame(tab_avg_rating, padding="20")
frame_avg_rating.grid(row=0, column=0)

# Botões e widgets - aba Aleatório
btn_random = ttk.Button(frame_random, text="Escolher Aleatório", command=show_random_deck)
btn_random.grid(row=0, column=0, padx=5, pady=5)

# Botões e widgets - aba Por Tipo
ttk.Label(frame_type, text="Tipo:").grid(row=0, column=0, sticky=tk.W)
tipos = sorted(set(deck["Tipo"] for deck in decks))  # Usando set para garantir tipos únicos
combo_tipo = ttk.Combobox(frame_type, values=tipos)
combo_tipo.grid(row=0, column=1, padx=5, pady=5)
combo_tipo.current(0)

btn_type = ttk.Button(frame_type, text="Escolher Deck", command=show_deck_by_type)
btn_type.grid(row=0, column=2, padx=5, pady=5)

# Botões e widgets - aba Por Personagem
ttk.Label(frame_character, text="Personagem:").grid(row=0, column=0, sticky=tk.W)
personagens = sorted(set(deck["Personagem"] for deck in decks))
combo_personagem = ttk.Combobox(frame_character, values=personagens)
combo_personagem.grid(row=0, column=1, padx=5, pady=5)
combo_personagem.current(0)

btn_character = ttk.Button(frame_character, text="Escolher Deck", command=show_deck_by_character)
btn_character.grid(row=0, column=2, padx=5, pady=5)

# Botões e widgets - aba Por Avaliação
ttk.Label(frame_rating, text="Critério:").grid(row=0, column=0, sticky=tk.W)
criterios = ["Consistência", "Diversão", "Ofensiva", "Defensiva"]
combo_criterio = ttk.Combobox(frame_rating, values=criterios)
combo_criterio.grid(row=0, column=1, padx=5, pady=5)
combo_criterio.current(0)

ttk.Label(frame_rating, text="Nota mínima:").grid(row=1, column=0, sticky=tk.W)
entry_nota = ttk.Entry(frame_rating, width=10)
entry_nota.grid(row=1, column=1, padx=5, pady=5)

btn_rating = ttk.Button(frame_rating, text="Escolher Deck", command=show_deck_by_rating)
btn_rating.grid(row=1, column=2, padx=5, pady=5)

# Botões e widgets - aba Por Média Geral
ttk.Label(frame_avg_rating, text="Média Geral mínima:").grid(row=0, column=0, sticky=tk.W)
entry_media = ttk.Entry(frame_avg_rating, width=10)
entry_media.grid(row=0, column=1, padx=5, pady=5)

btn_avg_rating = ttk.Button(frame_avg_rating, text="Escolher Deck", command=show_deck_by_average_rating)
btn_avg_rating.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
