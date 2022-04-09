# api-telegram


## Tecnologias utilizadas (Docs)
  * Python 3 (https://docs.python.org/3.8/)
  * Telegram API (https://core.telegram.org/)
  * TeleBotAPI (https://pypi.org/project/pyTelegramBotAPI/0.3.0/)
  * WS ViaCep (https://viacep.com.br/)
  
## Sobre o código
  * Para maior segurança utilizamos a variável de ambiente 'TOKEN_TELEGRAM'<br>
    ``` token = os.environ['TOKEN_LOCALIZA_BOT']```
  * O decorator @bot.message_handler foi utilizado para manipular as informações recebidas pelo chat. No codigo abaixo por exemplo foi utilizado para executar a função opcaoLocalizaCep assim que o comando consultarcep for recebido.<br>
  ```
    @bot.message_handler(commands=["consultarcep"])
     def opcaoLocalizaCep(mensagem):
          retornoCep = consultaCep(mensagem)
          bot.send_message(mensagem.chat.id, retornoCep)```
    
