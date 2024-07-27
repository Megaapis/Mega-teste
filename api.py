from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

criador = "Chupa cu"

def carregar_urls(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro de decodificação JSON no arquivo {arquivo}: {e}")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo {arquivo}: {e}")
        return []

urls = {
    "aesthetic": carregar_urls('db/aesthetic.json'),
    "ahegao": carregar_urls('db/ahegao.json'),
    "akira": carregar_urls('db/akira.json'),
    "ass": carregar_urls('db/ass.json'),
    "bonec": carregar_urls('db/bonek.json'),
    "Boruto": carregar_urls('db/boruto.json'),
    "cosplayloli": carregar_urls('db/cosplayloli.json'),
    "cosplay": carregar_urls('db/cosplay.json'),
    "cosplaysagirl": carregar_urls('db/cosplaysagiri.json'),
    "cum": carregar_urls('db/cum.json'),
    "Deidara": carregar_urls('db/deidara.json'),
    "Elaine": carregar_urls('db/elaina.json'),
    "Emilia": carregar_urls('db/emilia.json'),
    "ero": carregar_urls('db/ero.json'),
    "erza": carregar_urls('db/erza.json'),
    "feminotrava": carregar_urls('db/feminonotrava.json'),
    "foto18": carregar_urls('db/fotinhas.json'),
    "GameWallp": carregar_urls('db/GameWallp.json'),
    "Hinata": carregar_urls('db/hinata.json'),
    "itachi": carregar_urls('db/itachi.json'),
    "itori": carregar_urls('db/itori.json'),
    "Lolis": carregar_urls('db/lolis.json'),
    "Madara": carregar_urls('db/madara.json'),
    "manga": carregar_urls('db/manga.json'),
    "masturbation": carregar_urls('db/masturbation.json'),
    "meme": carregar_urls('db/meme.json'),
    "memes-video": carregar_urls('db/memes-video.json'),
    "mikasa": carregar_urls('db/mikasa.json'),
    "minato": carregar_urls('db/minato.json'),
    "neko": carregar_urls('db/neko.json'),
    "neko2": carregar_urls('db/neko2.json'),
    "nezuko": carregar_urls('db/nezuko.json'),
    "nsfwelisa": carregar_urls('db/nsfwelisa.json'),
    "nsfwlolis": carregar_urls('db/nsfwlolis.json'),
    "nsfwmia": carregar_urls('db/nsfwmia.json'),
    "onepiece": carregar_urls('db/onepiece.json'),
    "orgy": carregar_urls('db/orgy.json'),
    "pack": carregar_urls('db/pack.json'),
    "pokemon": carregar_urls('db/pokemon.json'),
    "pussy": carregar_urls('db/pussy.json'),
    "rize": carregar_urls('db/rize.json'),
    "rose": carregar_urls('db/rose.json'),
    "sagir": carregar_urls('db/sagiri.json'),
    "Sakura": carregar_urls('db/sakura.json'),
    "Sasuke": carregar_urls('db/sasuke.json'),
    "satanic": carregar_urls('db/satanic.json'),
    "shotas": carregar_urls('db/shotas.json'),
    "tentações": carregar_urls('db/tentacles.json'),
    "travazap": carregar_urls('db/travazap.json'),
    "Tsunade": carregar_urls('db/tsunade.json'),
    "vídeo+18": carregar_urls('db/videozinhos.json'),
    "waifu": carregar_urls('db/waifu.json'),
    "waifu2": carregar_urls('db/waifu2.json'),
    "wallhp2": carregar_urls('db/wallhp2.json'),
    "wallpapernime": carregar_urls('db/wallpapernime.json'),
    "zettai": carregar_urls('db/zettai.json'),
}

@app.route('/<category>', methods=['GET'])
def get_url(category):
    if category in urls:
        url_list = urls[category]
        if url_list:
            random_url = random.choice(url_list)
            response = {
                "status": True,
                "criador": criador,
                "url": random_url
            }
        else:
            response = {
                "status": False,
                "criador": criador,
                "código": 404,
                "mensagem": f"ei 🤨 Não Achei Nenhum Link De Imagem Na Categoria {category}"
            }
    else:
        response = {
            "status": False,
            "criador": criador,
            "código": 404,
            "mensagem": f"ei 🤨 Categoria {category} Não Encontrada"
        }

    return jsonify(response)
import os

PORT = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
