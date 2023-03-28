temp_index_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio - Dev</title>
    <style>
    .button {background-color: #008CBA;border: 2px solid #008CBA;color: #fff;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;}.button1 {padding: 10px 124px;}
    footer {display: block;text-align: center;margin-top:20%;padding: 3px;background-color: DarkSalmon;color: white;}
    </style>
</head>
<body>
    <div class="container" style="text-align: center;padding-top: 15px;">
        <h1>Operações Financeiras</h1>
        <a href="/web/form"><button class="button button1">UPLOAD ARQUIVO</button></a><br>
        <a href="/web/list"><button class="button button1">MOSTRAR OPERAÇÕES</button></a>
    </div>

    <footer>
        <p>Author: David Lucas<br>
        <a href="https://www.linkedin.com/in/david-lucas-souz4/">linkedin</a></p>
      </footer>
</body>
</html>"""

temp_form_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio - Dev</title>
    <style>.button {background-color: green;border: 2px solid #008CBA;color: #fff;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;}.button1 {padding: 10px 124px;}</style>
</head>
<body>
    <h1 style="text-align: center;">Área de Importação</h1>
    <div class="container" style="text-align: center;"><br>
        <form action="/web/upload" method="POST" enctype="multipart/form-data">
            <label for="myfile">Upload do arquivo CNAB:</label><br>
            <input type="file" id="myfile" name="myfile"><br><br>
            <input class="button button1" type="submit" value="Upload Arquivo" name="submit">
        </form>
        <br><br><a href="/">Voltar</a><br><br>
    </div>
    
</body>
</html>
"""

temp_form_error_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio - Dev - Process</title>
</head>
<body>
    <h2>Error ao processar arquivo...</h2>
    <a href="/">Voltar</a>
</body>
</html>
"""

temp_result_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio - Dev - Process</title>
</head>
<body>
    <h2>Arquivo processado ...</h2>
    <a href="/">Voltar</a>
</body>
</html>
"""

temp_list_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio - Dev</title>
<style>
tr:nth-child(even) {backgroundstyle}
</style>
</head>
<body>
    <h1 style="text-align: center;">Listagem de Operações</h1>
    <a href="/" style="text-align: right;">Voltar</a><br><br>
    <table style="font-family: arial,sans-serif;border-collapse:collapse;width:100%;">
        <tr>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">ID Transacao</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Tipo Transacao</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Descricao</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Natureza</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Data de Ocorrencia</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Valor</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">CPF</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Cartao</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Hora da Ocorrencia</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">ID Loja</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Nome da Loja</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Nome do representante</th>
          <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Saldo</th>
        </tr>
        {rg_li_html}
      </table>
</body>
</html>
"""

temp_li_html = """
<tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.id_transaction}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.type_transaction.id_type_transaction}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.type_transaction.description}</p>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.type_transaction.nature}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.date_occurrence}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">R$ {transaction.value}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.recipient.cpf}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.card.number}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.hour_occurrence}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.store.id_store}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.store.store_name}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">{transaction.store.store_owner}</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">R$ {transaction.store.balance}</td>
</tr>
"""
