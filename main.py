from logging import info
import discord
from discord.ext import commands
import os, random, requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот, я могу кидать тебе мемы про глобальное потепление а также могу расказать тебе что это такое и почему так происходит а также могу рассказать тебе как решить данную проблему! Мои команды: !command')

@bot.command()
async def command(ctx):
    await ctx.send(f'Мои команды: !hello, !mem, !info, !decision, !article')

@bot.command()
async def article(ctx):
    await ctx.send(f'Вот вам статья про глобальное потепление: https://clck.ru/39v4XU')

@bot.command()
async def decision(ctx):
    await ctx.send(f'Решение проблемы глобального потепления требует совместных усилий на глобальном уровне. Одним из ключевых моментов является снижение выбросов парниковых газов, особенно углекислого газа, за счет перехода к чистым источникам энергии и повышения энергоэффективности. Кроме того, необходимо активно защищать леса, которые играют важную роль в поглощении углекислого газа. Важным аспектом является также адаптация к изменению климата через разработку инфраструктуры, приспособленной к новым климатическим условиям. Международное сотрудничество и согласованные действия всех стран также необходимы для достижения значимых результатов. Образование и информирование общественности играют важную роль в формировании осознанного отношения к проблеме и стимулировании устойчивого образа жизни.')
  
@bot.command()
async def info(ctx):
    await ctx.send(f' Глобальное потепление - это явление увеличения средней температуры поверхности Земли в течение длительного времени. Это происходит из-за увеличения концентрации парниковых газов в атмосфере, таких как углекислый газ (CO2), метан, и оксиды азота. Эти газы препятствуют выходу тепла из атмосферы, что приводит к нагреву климата. Главные источники этих газов - это горение углеводородов (нефть, уголь, газ) для энергии и транспорта, а также разрушение лесов, которые обычно поглощают углекислый газ. Глобальное потепление вызывает ряд негативных последствий, таких как изменение погодных условий, повышение уровня морей, учащение экстремальных погодных явлений и угроза биоразнообразию и сельскому хозяйству.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
  
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
  
bot.run("TOKEN") 
