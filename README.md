# Customer propensity to purchase

**Propensão do cliente a comprar**

## Tópicos 

[Descrição](#Descrição)

[Dadaset](#Dadaset)

[Estrutura do Diretório](#Estrutura-do-Diretório)

[Ferramentas utilizadas](#Ferramentas-utilizadas)


## Descrição

Sabemos que lojas online recebe muitos visitantes todos os dias, mas grande parte dessas visitas não são convertidas em compras, muitas vezes nem retornam ao site.

Objetivo aqui é analisar informações referentes ao cliente em uma visita a uma loja online, e, implementendo um **modelo de classificação**, identificar os clientes com potencial de compra (se esse cliente vai realizar uma compra ou não).
Temos informações como:

    É um visitante novo ou ta retornando?
    Colocou produto no carrinho?
    Pesquisou sobre perguntas referente ao produto?
    Pesquisou sobre reclamações referente ao produto?
    O cliente ta acessando via celular, desktop ou tablet?

Quais dessas interações afetam a probabilidade de um usuário comprar? 

Tudo isso são informações que podem ser levadas em consideração para a implementação de um modelo de propensão a compra.

## Dadaset

Conjunto de dados que registra as interações dos compradores em uma loja online. É um desafio do kaggle, então pode ser baixado no link:

https://www.kaggle.com/benpowis/customer-propensity-to-purchase-data/code

Os dados de treinamento têm 455 mil interações de visitantes com um site fictício (representa o valor de um dia de visita).
Cada linha representa um cliente exclusivo, identificado por seu UserID exclusivo. 
As colunas representam características da visita dos usuários (como o dispositivo que eles estavam usando) e coisas que o usuário fez no site naquele dia. 
Esses recursos serão diferentes para cada site, mas nesses dados temos:

```
Colunas: Index(['UserID', 'basket_icon_click', 'basket_add_list', 'basket_add_detail',
       'sort_by', 'image_picker', 'account_page_click', 'promo_banner_click',
       'detail_wishlist_add', 'list_size_dropdown', 'closed_minibasket_click',
       'checked_delivery_detail', 'checked_returns_detail', 'sign_in',
       'saw_checkout', 'saw_sizecharts', 'saw_delivery', 'saw_account_upgrade',
       'saw_homepage', 'device_mobile', 'device_computer', 'device_tablet',
       'returning_user', 'loc_uk', 'ordered'],
      dtype='object')
```

Onde **UserID** é o id do cliente e **ordered** é a resposta se o cliente fez o pedido ou não


## Estrutura do Diretório
```
│   Customer propensity to purchase.ipynb  #script com EDA e teste com diferentes técnicas
│   Customer propensity_just model.py #script com implementação da técnica escolhida no jupyter notebook
│   README.md
│
└───dados
        testing_sample.csv
        training_sample.csv
```
## Ferramentas utilizadas
* Jupyter notebook
