import telebot

CHAVE_API = "7226680967:AAEwLBoUpghZJrCrC-w63svlNrxbgKA0BKE"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["1"])
def ops1(mensagem):
    texto = """
        O que você deseja?
        /pizza Pizza
        /hamburguer Hamburguer
        /salada Salada
    """
@bot.message_handler(commands=["pizza"])
def ops1(mensagem):
    texto = """
        Qual o sabor da pizza?
        /pizza1 Calabresa
        /pizza2 Bacon
        /pizza3 A moda
    """
@bot.message_handler(commands=["hamburguer"])
def ops1(mensagem):
    texto = """
        Qual tipo você deseja?
        /hamburguer1 Artesanal
        /hamburguer2 X-tudo
        /hamburguer3 
    """    
@bot.message_handler(commands=["2"])
def ops2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamacao@bps.com.br")

@bot.message_handler(commands=["3"])
def ops3(mensagem):
    print(mensagem)
    bot.reply_to(mensagem.chat.id,"Obrigado! Elogios são bem vindos!")


def verificar(mensagem):
    return True
    
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
        Escolha uma opção para continuar (Clique no item):
            /1 Fazer um pedido
            /2 Reclamar de um pedido
            /3 Realizar um elogio
            Responder qualquer outra coisa não vai funcionar, clique em uma das opções
            """
    bot.reply_to(mensagem, texto)


bot.polling()