import streamlit as st
import random
import string

st.set_page_config(page_title="Gerador de Senhas", page_icon="🔐")
st.title("🔐 Gerador de Senhas")

# Opções de caracteres
col1, col2, col3, col4 = st.columns(4)
with col1:
    usar_maiusculas = st.checkbox("A-Z", True)
with col2:
    usar_minusculas = st.checkbox("a-z", True)
with col3:
    usar_numeros = st.checkbox("0-9", True)
with col4:
    usar_simbolos = st.checkbox("!@#$%", True)

# Tamanho
tamanho = st.slider("Escolha o tamanho da senha:", 8, 32, 12)

def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    if not any([usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos]):
        return None

    caracteres = ""
    senha = []

    # Adicionar pelo menos um de cada tipo selecionado
    if usar_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        senha.append(random.choice(string.ascii_lowercase))
        caracteres += string.ascii_lowercase
    if usar_numeros:
        senha.append(random.choice(string.digits))
        caracteres += string.digits
    if usar_simbolos:
        senha.append(random.choice(string.punctuation))
        caracteres += string.punctuation

    # Preencher o restante da senha
    restante = tamanho - len(senha)
    senha += random.choices(caracteres, k=restante)
    random.shuffle(senha)
    return ''.join(senha)

# Gerar senha
if st.button("Gerar"):
    senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
    if senha:
        st.success("Senha gerada:")
        st.code(senha, language="bash")
        st.write("✅ Copie e use a senha gerada.")
    else:
        st.error("Selecione pelo menos um tipo de caractere!")
