import os

import telebot
import random

from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['nickfaigliauguri'])
def sign_handler(message): 
	sent_msg = bot.send_message(message.chat_id, 'Auguri terrone')

@bot.message_handler(commands=['nick'])
def sign_handler(message):
    resp = [
	"Ma andiamo nel bosco, di notte e fatti. Ma voi siete pazzi?", 
	"Ma dove andiamo, arriviamo alle mucche?", 
	"E poi se uno sta male e sviene tipo Nick Banin?", 
        "Accettiamo proprio tutti qua dentro eh", 
        "Sotto il piave tutti terroni", 
        "Non permetterti di parlare così di mio fratello Carone", 
        "Discorsetto?", 
        "21 fiocchi di neve per favore", 
        "SAVERIO STA CADENDO IL CIELO E TU PENSI ALLA MENSA", 
        "Quella agua de Pisa, quella maledetta agua de Pisa", 
        "Napoli? Non conosco...", 
        "Bello ma non è Balzola", 
        "Vah che andiamo all'estero eh", 
        "Ma chi è sto coglione?", 
        "Lui viene sicuramente da Zurigo", 
        "Eh la Filomena...", 
        "Facciamogli l'inganno della cadrega", 
        "Te sei un fantasista", 
        "Amici grazie della serata vvb", 
        "Devo ancora alzarmi dal letto, però ci metto poco 🤡",
        "RAGA HO VINTO UN BOMBOLÒ", 
        "scusate eh ma MIMMODONG chi è?", 
        "Gianni davvero ti stai mettendo in imbarazzo", 
        "Che luogo incredibile il sud Italia", 
	"Nascondiamola dove Carone non arriva"
    ]
    a = random.randint(1, len(resp)) - 1
    sent_msg = bot.send_message(message.chat.id, resp[a])

@bot.message_handler(commands=['insegnamiilnapoletano'])
def sign_handler(message):
    resp = [
        "arrubbà 'a casa ro' mariuòlo\n\nDetto napoletano per: \n\"Non puoi fregare chi è più furbo di te\"", 
        "Cù na man annanz e nata arrèt\n\nDetto napoletano per: \n\"Colui che resta deluso dalle situazioni e rimane fregato\"", 
        "Vulè ò cocco ammunnàto e bbuòno\n\nDetto napoletano per: \n\"Volere tutto bello e pronto\"", 
        "'O barbière te fa bello, 'o vino te fa guàppo, 'a fèmmena te fa fesso\n\nDetto napoletano autoesplicativo", 
        "A murì pe' campà\n\nDetto napoletano per: \n\"Sei una persona inutile\"", 
        "Scem 'e 'uerra\n\nDetto napoletano per: \n\"Rifetito a uno stolto\"", 
        "Fa 'a fine 'e Fetacchièllo\n\nDetto napoletano per: \n\"Fallire clamorosamente\"", 
        "uagliò bell' stu regàlo\n\nDetto napoletano per: \n\"Esprime gratitudine verso un presente ricevuto\""
    ]
    a = random.randint(1, len(resp)) - 1
    sent_msg = bot.send_message(message.chat.id, resp[a])

bot.infinity_polling()