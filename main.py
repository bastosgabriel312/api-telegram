import telebot
import os
import json
import requests

token = os.environ['TOKEN_LOCALIZA_BOT']
bot = telebot.TeleBot(token)


def cepJson2String(jsonCep):
    text = f"""CEP: {jsonCep['cep']}\n
Endereço: {jsonCep['logradouro']}\n
Bairro: {jsonCep['bairro']}\n
Cidade: {jsonCep['localidade']}\n
UF: {jsonCep['uf']}
"""
    return text


def consultaCep(mensagem):
    reportCep = 'CEP inválido por favor insira novamente /consultacep [Seu CEP]'
    # Trata o indexError proveniente da entrada do comando /consultacep sem um cep
    try:
        cep = mensagem.text.split(' ')[1]
        url_cep = f"https://viacep.com.br/ws/{cep}/json/"
        req = requests.get(url_cep)
        # realiza  a consulta somente se o status code for igual a 200 (OK)
        if req.status_code == 200:
    	    dados_json = json.loads(req.text)
    	    # Tratamento para CEP inserido como 00000002, retorna 200 porém com um json com erro:true
    	    if not 'erro' in dados_json:
    	        # Retorna o json formatado para string
    	        return cepJson2String(dados_json)
        return reportCep
    except IndexError:
        return reportCep




@bot.message_handler(commands=["consultarcep"])
def opcaoLocalizaCep(mensagem):
    retornoCep = consultaCep(mensagem)
    bot.send_message(mensagem.chat.id, retornoCep)



####################### Inicia com essa mensagem ###################
@bot.message_handler()
def responder(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Ir até o repositório', url='https://github.com/bastosgabriel312/api-telegram'
       )
   )
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Fale com um representante', url='telegram.me/bastosgabriel312'
       )
   )

   bot.send_message(
       message.chat.id,
       ' SEJA BEM VINDO A CONSULTA DE ENDEREÇO  \n\n' +
       '- Para Consultar CEP envie /consultarcep [seu CEP] Somente numeros\n'+
       '- Exemplo /consultarcep 01010000',
       reply_markup=keyboard
   )


# Executa bot em looping
bot.polling()
