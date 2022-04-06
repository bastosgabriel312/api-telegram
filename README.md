# api-telegram


## Tecnologias utilizadas
  * Python 3 (https://docs.python.org/3.8/)
  * Telegram API (https://core.telegram.org/)
  * API ViaCep (https://viacep.com.br/)
  
## Sobre o código
  * Para maior segurança utilizamos a variável de ambiente 'TOKEN_TELEGRAM'<br>
    ``` token = os.environ['TOKEN_TELEGRAM']```
  * O message_handler foi utilizado para capturar os comandos efetuados no chat<>
  ```@bot.message_handler(commands=["consultarcep"])
     def opcaoLocalizaCep(mensagem):
          retornoCep = consultaCep(mensagem)
          bot.send_message(mensagem.chat.id, retornoCep)```
    
