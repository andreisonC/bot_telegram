import requests
import telebot
import time


CHAVE_API = '5682296657:AAGyAtFZdxBkWkKa8QY1Z5_7L1-9E0KsmIs'


bot = telebot.TeleBot(CHAVE_API)

print('BOT INICIADO!')

@bot.message_handler(commands=['cep'])
def responder(mensagem):
    qnt = len(mensagem.text)
    qnt2 = qnt - 5
    if qnt2 < 0:
        qntd = '0'
    else:
        qntd = qnt2
    if len(mensagem.text) != 13:
        bot.reply_to(mensagem,f'Quantidade de numero invalida: {qntd}')
        bot.send_message(mensagem.chat.id,'Insira novamente o cep')
    else:
        cep = (mensagem.text[5:])
        request = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
        address_data = request.json()
        if 'status' not in address_data:
                bot.reply_to(mensagem,f'''
ã¤ã¤ã¤ã¤ð CEP ENCONTRADO ð
TIPO: {(address_data['address_type'])}  
CEP: {(address_data['cep'])}  
RUA: {(address_data['address_name'])}   
BAIRRO: {(address_data['district'])}   
CIDADE/UF: {(address_data['city'])}/{(address_data['state'])}
DDD: {(address_data['ddd'])}
LAT: {(address_data['lat'])}
LNG: {(address_data['lng'])}
IBGE: {(address_data['city_ibge'])}   
solicitado por: {mensagem.chat.first_name}
''')
        else:   
            request = requests.get(
            f'https://viacep.com.br/ws/{cep}/json')
            address_data2 = request.json()
            time.sleep(1)
            if 'erro' not in address_data2:
                    bot.reply_to(mensagem,f'''
ã¤ã¤ã¤ã¤ã¤ð CEP ENCONTRADO ð
 
CEP: {(address_data2['cep'])}          
RUA: {(address_data2['logradouro'])}       
BAIRRO: {(address_data2['bairro'])}       
CIDADE/UF: {(address_data2['localidade'])}/{(address_data2['uf'])}
DDD: {(address_data2['ddd'])}
''')
            else:
                bot.reply_to(mensagem,f'â ï¸ CEP NÃO ENCONTRADO! â ï¸: {cep}')

@bot.message_handler(commands=['cnpj'])
def responder(mensagem):
    qnt = len(mensagem.text)
    qnt1 = qnt - 6
    if qnt1 < 0:
        qntd = '0'
    else:
        qntd = qnt1
    if len(mensagem.text) != 20:
        bot.reply_to(mensagem,f'Quantidade de numero invalida: {qntd}')
        bot.send_message(mensagem.chat.id,'Insira novamente o cnpj')
    else:
        cnpj = (mensagem.text[6:])
        cnrequest = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
        cnaddress_data = cnrequest.json()
        status = cnrequest
        if 'message' in cnaddress_data:
            bot.reply_to(mensagem,f'â ï¸ CNPJ NÃO ENCONTRADO! â ï¸: {cnpj}')
        if status == '<Response [429]>':
            bot.reply_to(mensagem,'To many requests! ')

        else:
            bot.reply_to(mensagem,f'''
ã¤ã¤ã¤ã¤ã¤ð CNPJ ENCONTRADO ð
â¢ CNPJ:  {cnpj}              
â¢ TIPO: {(cnaddress_data['tipo'])} 

â¢ ABERTURA:  {(cnaddress_data['abertura'])}   


â¢ NOME:  {(cnaddress_data['nome'])}

â¢ NOME FANTASIA:  {(cnaddress_data['fantasia'])} 
â¢ PORTE:  {(cnaddress_data['porte'])} 

â¢ CÃDIGO E ATIVIDADE PRINCIPAL: {(cnaddress_data['atividade_principal'])} 

â¢ CÃDIGO E ATIVIDADES SECUNDÃRIAS: {(cnaddress_data['atividades_secundarias'])} 

â¢ CÃDIGO E NATUREZA JURÃDICA:  {(cnaddress_data['natureza_juridica'])} 

â¢ QUADRO DE SÃCIOS E ADMINISTRADORES:  

â¢ LOGRADOURO:  {(cnaddress_data['logradouro'])}
â¢ NÃMERO:  {(cnaddress_data['numero'])}
â¢ COMPLEMENTO:  {(cnaddress_data['complemento'])}

â¢ CEP:  {(cnaddress_data['cep'])} 
â¢ BAIRRO/DISTRITO:  {(cnaddress_data['bairro'])} 
â¢ MUNICÃPIO:  {(cnaddress_data['municipio'])}  
â¢ ESTADO:  {(cnaddress_data['uf'])} 

â¢ TELEFONE:  {(cnaddress_data['telefone'])}
â¢ EMAIL:  {(cnaddress_data['email'])}

â¢ STATUS:  {(cnaddress_data['status'])}

â¢ ÃLTIMA ATUALIZAÃÃO: {(cnaddress_data['ultima_atualizacao'])} 

â¢ EFR:  {(cnaddress_data['efr'])} 

â¢ SITUAÃÃO CADASTRAL:  {(cnaddress_data['situacao'])} 

â¢ MOTIVO DE SITUAÃÃO CADASTRAL:  {(cnaddress_data['motivo_situacao'])} 

â¢ SITUAÃÃO ESPECIAL:  {(cnaddress_data['situacao_especial'])} 
â¢ DATA DA SITUAÃÃO ESPECIAL:  {(cnaddress_data['data_situacao_especial'])} 

â¢ CAPITAL SOCIAL:  {(cnaddress_data['situacao_especial'])}''')

bot.polling()
