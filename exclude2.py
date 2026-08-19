import pyautogui as pa # Biblioteca para controlar mouse e teclado.

import time  # Biblioteca para controlar pausas.

pa.PAUSE = 1  # Pausa automática de 1 segundo após cada ação do PyAutoGUI.

# ==============================
# CONFIGURAÇÕES
# ==============================

QUANTIDADE = 5  # Quantidade de contatos a excluir.

TEMPO_INICIAL = 5  # Tempo para posicionar a página antes de iniciar.

ESPERA_MODAL = 2 # Tempo para o modal de confirmação aparecer.

ESPERA_PAGINA = 8 # Tempo para a página atualizar após a exclusão.

BOTAO_EXCLUIR = (-430, 671) # Coordenada do botão "Excluir" do contato.

BOTAO_CONFIRMAR = (-994, 388) # Coordenada do botão "Excluir" do modal.

# ==============================
# INÍCIO
# ==============================

print("=" * 40)
print("EXCLUSÃO AUTOMÁTICA DE CONTATOS")
print("=" * 40)

print(f"Quantidade programada: {QUANTIDADE}")
print(f"Você tem {TEMPO_INICIAL} segundos para posicionar a página.")

time.sleep(TEMPO_INICIAL)  # Aguarda o tempo inicial antes de começar.

# ==============================
# LAÇO
# ==============================

for i in range(QUANTIDADE):  # Repete o processo pela quantidade definida.

    print()
    print(f"--- CONTATO {i + 1} DE {QUANTIDADE} ---")

    print("Posição do mouse:", pa.position()) # Mostra a posição atual do mouse.

    print("Clicando em Excluir...")
    pa.click(x=BOTAO_EXCLUIR[0], y=BOTAO_EXCLUIR[1]) # Clica no botão "Excluir" do contato.

    print(f"Aguardando modal ({ESPERA_MODAL}s)...")   # Aguarda o modal abrir.
    time.sleep(ESPERA_MODAL)

    print("Confirmando exclusão...") # Clica no botão "Excluir" do modal.
    pa.click(
        x=BOTAO_CONFIRMAR[0],
        y=BOTAO_CONFIRMAR[1]
    )
    
    print(f"Aguardando atualização ({ESPERA_PAGINA}s)...") # Aguarda a Locaweb processar a exclusão.
    time.sleep(ESPERA_PAGINA)

    print(f"Contato {i + 1} concluído.")  # Informa que a exclusão terminou.

print()
print("=" * 40)
print("PROCESSO FINALIZADO")
print(f"{QUANTIDADE} exclusões executadas.")
print("=" * 40)