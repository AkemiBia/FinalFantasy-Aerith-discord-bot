import discord
import random
from discord.ext import commands
from serpapi import GoogleSearch

# Configuração do bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Chave da API SerpAPI
SERPAPI_KEY = "key"

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} está online!")

@bot.command()
async def aerith(ctx):
    """Busca uma imagem aleatória da Aerith no Google Imagens e envia no Discord"""
    try:
        search = GoogleSearch({
            "q": "Aerith Gainsborough Final Fantasy",
            "tbm": "isch",  # Pesquisa por imagens
            "ijn": "0",
            "api_key": SERPAPI_KEY
        })
        results = search.get_dict()  # CORRIGIDO
        
        imagens = [img["original"] for img in results.get("images_results", [])]
        
        if imagens:
            imagem = random.choice(imagens)
            await ctx.send(imagem)
        else:
            await ctx.send("Não encontrei imagens da Aerith no momento 😢")

    except Exception as e:
        await ctx.send(f"Erro ao buscar imagem: {e}")

# Rodar o bot (substitua pelo seu token do Discord)
bot.run("bot_token")
