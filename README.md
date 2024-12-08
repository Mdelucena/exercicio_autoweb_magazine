Como usar
Clone o repositório ou baixe o código em uma pasta local.

Instale as dependências: No terminal, dentro da pasta do projeto, execute:

bash
Copiar código
pip install selenium
Abra o arquivo auto.py e verifique se o ChromeDriver está corretamente configurado para o seu sistema (verifique o caminho para o chromedriver).

Execute o script: Execute o script com o comando:

bash
Copiar código
python auto.py
Ações automatizadas:

O script abrirá o navegador Chrome.
Acessará o site da Magazine Luiza.
Esperará que o botão "Informações Financeiras" seja visível e clicará nele.
Depois, clicará no link "Planilha de Resultado" e, em seguida, no link "Planilha de Resultados Trimestrais" para iniciar o download.
Finalizando: O download será iniciado e o navegador será fechado automaticamente após a execução do script.

Explicação do Código
O script realiza as seguintes ações:

Inicializa o navegador: O navegador Chrome é aberto e maximizado.
Esperas dinâmicas: Usando WebDriverWait, o script aguarda até que os elementos desejados estejam visíveis antes de interagir com eles.
Interações com os elementos:
Localiza o botão "Informações Financeiras" e clica nele.
Após acessar a página de resultados, clica nos links "Planilha de Resultado" e "Planilha de Resultados Trimestrais".
Download da planilha: O arquivo da planilha será baixado automaticamente no diretório padrão de downloads do navegador.
Observações
O script depende do ChromeDriver para funcionar corretamente. Certifique-se de que a versão do ChromeDriver é compatível com a versão do Google Chrome instalada no seu computador.
O download será feito no diretório padrão de downloads do navegador. Se desejar configurar o caminho de download, você pode adicionar configurações extras no chrome_options do Selenium.
Caso queira modificar o comportamento do script, como tempo de espera ou os links clicados, basta ajustar o código conforme necessário.
Licença
Este projeto é de código aberto e pode ser usado, modificado e distribuído livremente, conforme necessário.
