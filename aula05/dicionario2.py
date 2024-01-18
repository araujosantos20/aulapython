import os
os.system("clear")

capitais = {
    "acre":"rio branco",
    "amapá":"macapá",
    "amazona":"manaus",
    "bahia":"salvador",
    "ceará":"fortaleza",
    "espirito santo":"vitoria",
    "goias":"goiânia",
    "maranhao":"sao luis",
    "mato grosso":"cuiaba",
    "mato grosso do sul":"campo grande",
    "minas gerais":"belo horizonte",
    "pará":"belem",
    "paraiba":"joao pessoa",
    "parana":"curitiba",
    "pernambuco":"recife",
    "piaui":"teresina",
    "rio de janeiro":"rio de janeiro",
    "rio grande do norte":"natal",
    "rio grande do sul":"porto alegre",
    "rondonia":"porto velho",
    "roraima":"boa vista",
    "santa catarina":"florianópolis",
    "são paulo":"são paulo",
    "sergipe":"aracaju",
    "tocantins":"palmas",
    "distrito federal":"brasilia",
}

# for i in capitais:
#     print(i)

# print(capitais[0:6])

# print(capitais["acre"])

ps = 1
for i in capitais:
    if ps< 6:
     print(i + " A capital é " +capitais[i])
    else:
       break
    ps += 1

