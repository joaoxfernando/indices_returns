# O Projeto!

Esse projeto irá calcular o retorno de alguns índices de bolsas de valores pelo mundo a fora.


# Quais índices ele irá calcular?

A princípio, ele irá calcular os retornos dos índices abaixo:
- Ibovespa: Brasil
- Nasdaq: EUA (Tecnologia)
- S&P 500: EUA (500 maiores)
- Down Jones: EUA
- FTSE 100: Reino Unido (100 maiores)
- ESTX 50 PR.EUR: Europa (50 maiores da zona do Euro)
- EURONEXT 100: Europa (100 maiores)
- Merval: Argentina
- Nikkei 225: Japão
- CSI 300: China

# Como rodar
Antes de executar pela primeira vez, abra o terminal dentro do diretório do projeto e rode um dos seguintes comandos:

```bash
pip install -r requirements.txt
```

```bash
python -m pip install -r requirements.txt
```
Em seguida você pode rodar o notebook indicadores.ipynb

Caso queira personalizar, você pode alterar os parametros na função **matplotlib_plot** dentro do arquivo plot.py. Para obter a lista de estilos disponíveis, você pode executar o arquivo **get_styles.ipynb** ou consultar diretamente na [documentação do matplotlib](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

Caso queira adicionar algum índice, você pode incluir na lista no ínicio do arquivo indicadores.ipynb, lá tem um trecho com a orientação de como inseri-lo. Lembrando que como é utilizada a biblioteca do yfinance (Yahoo Finance), é necessário que o índice esteja disponível lá.

Devido a grande variedade de índices, os retornos de cada um está sendo calculado na sua moeda, logo, outros indicadores econômicos deverão ser levado em conta para um veredito final sobre a rentabilidade, já que países como Argentina pode ter um retorno bem elevado, mas é necessário dados como inflação, variação cambial, etc., para determinar se o investimento seria lucrativo ou não.

Em breve pretendo realizar alguns upgrades no projeto para permitir maior personalização da janela de tempo, mas no trecho **Analisando um período maior** é possível definir manualmente a data de ínicio e fim da análise, logo, fiquem a vontade para brincar com essas informações. Lembrando que quanto mais antiga a data, maior a chance de não ter dados suficientes para todos os índices e a comparação se torna inviável.