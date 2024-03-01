import streamlit as st

# Define a function to calculate CPA
def calculate_cpa(faturamento, despesas, num_vendas, num_leads=None):
    lucro = faturamento - despesas
    cpa = lucro / num_vendas
    if num_leads > 0:
        cpa = cpa / num_leads
    meta_cpa = round(cpa / 2, 2)
    metinha_cpa = round((cpa/2) * 1.5, 2)
    metao_cpa = round((cpa/2) * 0.5, 2)
    return cpa, metinha_cpa, meta_cpa, metao_cpa

# Create a Streamlit app
st.title("Calculadora de CPA")

# Create input fields for the user to enter the values
faturamento = st.number_input("Insira o valor de faturamento", value=0.0, step=0.01)
despesas = st.number_input("Insira o valor de despesas", value=0.0, step=0.01)
num_vendas = st.number_input("Insira o número de vendas", value=0.0, step=0.01)
num_leads = st.number_input("Insira o número de leads (opcional)", value=0.0, step=0.01)

# Create a button to calculate CPA when clicked
if st.button("Calcular CPA"):
    cpa, metinha_cpa, meta_cpa, metao_cpa = calculate_cpa(faturamento, despesas, num_vendas, num_leads)
    st.write("O lucro por venda:", "R$"+ " "+ str(cpa))
    st.write("A metinha do CPA é de: ", "R$"+ " "+ str(metinha_cpa))
    st.write("A meta do CPA é de: ", "R$"+ " "+ str(meta_cpa))
    st.write("O metão do CPA é de: ", "R$"+ " "+ str(metao_cpa))