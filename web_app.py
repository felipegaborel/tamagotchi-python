# Minimal Flask web interface for Tamagotchi (for testing)
# Requires: Flask

from flask import Flask, request, jsonify, render_template_string, redirect, url_for
from animals.animal import Animal
from animals.cat import Cat
from animals.dog import Dog
from animals.dragon import Dragon
from animals.rabbit import Rabbit

app = Flask(__name__)

# Simple in-memory store for a single session pet (for testing only)
PET = {"obj": None}

INDEX_HTML = """
<!doctype html>
<title>Tamagotchi Web</title>
<h1>Tamagotchi (Web Test)</h1>
{% if pet %}
  <h2>{{ pet.nome }} ({{ pet.__class__.__name__ }})</h2>
  <p>Saúde: {{ pet.health }} | Fome: {{ pet.hunger }} | Energia: {{ pet.energy }} | Felicidade: {{ pet.happiness }}</p>
  <form action="/action" method="post">
    <button name="act" value="feed">Alimentar</button>
    <button name="act" value="play">Brincar</button>
    <button name="act" value="sleep">Dormir</button>
    <button name="act" value="bath">Banho</button>
    <button name="act" value="save">Salvar</button>
  </form>
{% else %}
  <form action="/create" method="post">
    Nome: <input name="name" />
    <select name="type">
      <option value="dog">Cachorro</option>
      <option value="cat">Gato</option>
      <option value="rabbit">Coelho</option>
      <option value="dragon">Dragão</option>
    </select>
    <button type="submit">Criar</button>
  </form>
{% endif %}
"""

@app.route('/', methods=['GET'])
def index():
    pet = PET['obj']
    return render_template_string(INDEX_HTML, pet=pet)

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name', 'Mochi')
    t = request.form.get('type', 'dog')
    cls = {'dog': Dog, 'cat': Cat, 'rabbit': Rabbit, 'dragon': Dragon}.get(t, Dog)
    PET['obj'] = cls(name)
    return redirect(url_for('index'))

@app.route('/action', methods=['POST'])
def action():
    pet = PET['obj']
    if not pet:
        return redirect(url_for('index'))
    act = request.form.get('act')
    if act == 'feed':
        pet.feed()
    elif act == 'play':
        pet.play()
    elif act == 'sleep':
        pet.sleep()
    elif act == 'bath':
        pet.bath()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
