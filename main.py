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
ㅤㅤㅤㅤ🔍 CEP ENCONTRADO 🔎
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
ㅤㅤㅤㅤㅤ🔍 CEP ENCONTRADO 🔎
 
CEP: {(address_data2['cep'])}          
RUA: {(address_data2['logradouro'])}       
BAIRRO: {(address_data2['bairro'])}       
CIDADE/UF: {(address_data2['localidade'])}/{(address_data2['uf'])}
DDD: {(address_data2['ddd'])}
''')
            else:
                bot.reply_to(mensagem,f'⚠️ CEP NÃO ENCONTRADO! ⚠️: {cep}')

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
            bot.reply_to(mensagem,f'⚠️ CNPJ NÃO ENCONTRADO! ⚠️: {cnpj}')
        if status == '<Response [429]>':
            bot.reply_to(mensagem,'To many requests! ')

        else:
            bot.reply_to(mensagem,f'''
ㅤㅤㅤㅤㅤ🔍 CNPJ ENCONTRADO 🔎
• CNPJ:  {cnpj}              
• TIPO: {(cnaddress_data['tipo'])} 

• ABERTURA:  {(cnaddress_data['abertura'])}   


• NOME:  {(cnaddress_data['nome'])}

• NOME FANTASIA:  {(cnaddress_data['fantasia'])} 
• PORTE:  {(cnaddress_data['porte'])} 

• CÓDIGO E ATIVIDADE PRINCIPAL: {(cnaddress_data['atividade_principal'])} 

• CÓDIGO E ATIVIDADES SECUNDÁRIAS: {(cnaddress_data['atividades_secundarias'])} 

• CÓDIGO E NATUREZA JURÍDICA:  {(cnaddress_data['natureza_juridica'])} 

• QUADRO DE SÓCIOS E ADMINISTRADORES:  

• LOGRADOURO:  {(cnaddress_data['logradouro'])}
• NÚMERO:  {(cnaddress_data['numero'])}
• COMPLEMENTO:  {(cnaddress_data['complemento'])}

• CEP:  {(cnaddress_data['cep'])} 
• BAIRRO/DISTRITO:  {(cnaddress_data['bairro'])} 
• MUNICÍPIO:  {(cnaddress_data['municipio'])}  
• ESTADO:  {(cnaddress_data['uf'])} 

• TELEFONE:  {(cnaddress_data['telefone'])}
• EMAIL:  {(cnaddress_data['email'])}

• STATUS:  {(cnaddress_data['status'])}

• ÚLTIMA ATUALIZAÇÃO: {(cnaddress_data['ultima_atualizacao'])} 

• EFR:  {(cnaddress_data['efr'])} 

• SITUAÇÃO CADASTRAL:  {(cnaddress_data['situacao'])} 

• MOTIVO DE SITUAÇÃO CADASTRAL:  {(cnaddress_data['motivo_situacao'])} 

• SITUAÇÃO ESPECIAL:  {(cnaddress_data['situacao_especial'])} 
• DATA DA SITUAÇÃO ESPECIAL:  {(cnaddress_data['data_situacao_especial'])} 

• CAPITAL SOCIAL:  {(cnaddress_data['situacao_especial'])}''')

bot.polling()
