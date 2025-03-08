import requests
import tkinter as tk
from PIL import Image, ImageTk
import io


def buscar_pokemon():
    pokemon_name = entry.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        imagen_url = data["sprites"]["front_default"]
        response_img = requests.get(imagen_url)
        img_data = response_img.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((150, 150))
        pokemon_image = ImageTk.PhotoImage(img)
        image_label.config(image=pokemon_image)
        image_label.image = pokemon_image
        result_label.config(text=f"{data['name'].capitalize()}\n{data['id']}\n{data['height']}\n{data['weight']}\n{', '.join([tipo['type']['name'].capitalize() for tipo in data['types']])}")
    else:
        result_label.config(text="No encontrado.")

window = tk.Tk()
window.title("Pokédex")
entry = tk.Entry(window)
entry.pack(pady=10)
search_button = tk.Button(window, text="Buscar", command=buscar_pokemon)
search_button.pack()
result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)
image_label = tk.Labe