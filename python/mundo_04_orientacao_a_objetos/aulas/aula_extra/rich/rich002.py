from rich import print # Prints com cores e emojis
from rich.panel import Panel # Painéis

caixa = Panel("[purple] Esse aqui é um painel de exemplo [/purple] :+1:", title="Mensagem", style="violet", width= 30)

print(caixa)