
from openai import OpenAI
from config import QWEN_API_KEY

# Ligação à API Qwen
client = OpenAI(
    api_key=QWEN_API_KEY,
    base_url="https://ap-southeast-1.maas.qwencloudapi.com/compatible-mode/v1",
    timeout=60.0,
    max_retries=2
)

# Personalidade do NEXA
SYSTEM_PROMPT = """
O teu nome é NEXA.

És um assistente pessoal inteligente, profissional,
prestável e eficiente.

Falas português de forma natural.
Respondes de maneira clara, organizada e objetiva.

Ajudas o utilizador a:
- Organizar tarefas.
- Analisar informações.
- Resumir conversas.
- Resolver problemas.
- Gerir atividades pessoais e profissionais.

Mantém sempre o contexto da conversa.
"""

# Histórico da conversa
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def iniciar_nexa():
    print("\n================================")
    print("         NEXA ASSISTANT")
    print("================================")
    print("Inteligência artificial: Qwen")
    print("Estado: Online")
    print("Escreve 'sair' para terminar.")
    print("================================\n")

    while True:
        mensagem = input("Tu: ").strip()

        if mensagem.lower() == "sair":
            print("\nNEXA: Até à próxima!")
            break

        if not mensagem:
            continue

        messages.append({
            "role": "user",
            "content": mensagem
        })

        try:
            print("\nNEXA está a pensar...\n")

            response = client.chat.completions.create(
                model="qwen3.8-max",
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )

            resposta = response.choices[0].message.content

            if not resposta:
                print("NEXA: Não recebi uma resposta válida.")
                messages.pop()
                continue

            messages.append({
                "role": "assistant",
                "content": resposta
            })

            print("NEXA:", resposta, "\n")

        except Exception as erro:
            messages.pop()
            print("Erro na ligação à Qwen API:")
            print(type(erro).__name__, erro, "\n")


if __name__ == "__main__":
    iniciar_nexa()
