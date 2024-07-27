from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

# Criador da API
criador = "Come-tias"

# Função para carregar URLs de um arquivo JSON
def load_urls(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Dicionário de categorias e seus arquivos
categories = {
    'aesthetic': 'db/aesthetic.json',
    'ahegao': 'db/ahegao.json',
    'akira': 'db/akira.json',
    'ass': 'db/ass.json',
    'bonec': 'db/bonec.json',
    'Boruto': 'db/Boruto.json',
    'cosplayloli': 'db/cosplayloli.json',
    'cosplay': 'db/cosplay.json',
    'cosplaysagirl': 'db/cosplaysagirl.json',
    'cum': 'db/cum.json',
    'Deidara': 'db/Deidara.json',
    'Elaine': 'db/Elaine.json',
    'Emilia': 'db/Emilia.json',
    'ero': 'db/ero.json',
    'erza': 'db/erza.json',
    'feminotrava': 'db/feminotrava.json',
    'foto18': 'db/foto18.json',
    'GameWallp': 'db/GameWallp.json',
    'Hinata': 'db/Hinata.json',
    'itachi': 'db/itachi.json',
    'itori': 'db/itori.json',
    'Lolis': 'db/Lolis.json',
    'Madara': 'db/Madara.json',
    'manga': 'db/manga.json',
    'masturbation': 'db/masturbation.json',
    'meme': 'db/meme.json',
    'memes-video': 'db/memes-video.json',
    'mikasa': 'db/mikasa.json',
    'minato': 'db/minato.json',
    'neko': 'db/neko.json',
    'neko2': 'db/neko2.json',
    'nezuko': 'db/nezuko.json',
    'nsfwelisa': 'db/nsfwelisa.json',
    'nsfwlolis': 'db/nsfwlolis.json',
    'nsfw': 'db/nsfw.json',
    'mia': 'db/mia.json',
    'onepiece': 'db/onepiece.json',
    'orgy': 'db/orgy.json',
    'pack': 'db/pack.json',
    'pokemon': 'db/pokemon.json',
    'pussy': 'db/pussy.json',
    'rize': 'db/rize.json',
    'rose': 'db/rose.json',
    'sagir': 'db/sagir.json',
    'Sakura': 'db/Sakura.json',
    'Sasuke': 'db/Sasuke.json',
    'satanic': 'db/satanic.json',
    'shotas': 'db/shotas.json',
    'tentações': 'db/tentações.json',
    'travazap': 'db/travazap.json',
    'Tsunade': 'db/Tsunade.json',
    'vídeo+18': 'db/vídeo+18.json',
    'waifu': 'db/waifu.json',
    'waifu2': 'db/waifu2.json',
    'wallhp2': 'db/wallhp2.json',
    'wallpapernime': 'db/wallpapernime.json',
    'zettai': 'db/zettai.json'
}

@app.route('/api/<category>', methods=['GET'])
def get_random_url(category):
    if category not in categories:
        return jsonify({
            'error': {
                'status': False,
                'criador': criador,
                'mensagem': 'ops :/ ocorreu um erro no servidor, tente novamente mais tarde'
            }
        }), 404

    try:
        urls = load_urls(categories[category])
        if not urls:
            return jsonify({
                'cdimg': {
                    'status': False,
                    'criador': criador,
                    'código': 404,
                    'mensagem': 'ei 🤨 Nao Achei Nenhum Link De Imagem Na Url'
                }
            }), 404
        url = random.choice(urls)
        return jsonify({
            'url': url,
            'status': True,
            'criador': criador
        })
    except Exception as e:
        return jsonify({
            'error': {
                'status': False,
                'criador': criador,
                'mensagem': 'ops :/ ocorreu um erro no servidor, tente novamente mais tarde'
            }
        }), 500

if __name__ == '__main__':
    app.run(debug=True
