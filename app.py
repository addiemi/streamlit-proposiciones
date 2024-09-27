import streamlit as st

def P(x):
    """Función proposicional: devuelve True si x es par, False en caso contrario."""
    return x % 2 == 0

def get_domain(start=1, end=10):
    """Devuelve el dominio de evaluación."""
    return list(range(start, end + 1))

def forall(domain, predicate):
    """Evalúa la proposición universal: ∀x ∈ dominio, P(x)."""
    return all(predicate(x) for x in domain)

def exists(domain, predicate):
    """Evalúa la proposición existencial: ∃x ∈ dominio, P(x)."""
    return any(predicate(x) for x in domain)

def main():
    st.set_page_config(page_title="Proposiciones Cuantificadas", layout="centered")
    
    st.title("📚 Funciones Proposicionales y Cuantificadores")
    
    st.sidebar.header("🔧 Configuración del Dominio")
    
    start = st.sidebar.number_input("Inicio del Dominio", value=1, step=1)
    end = st.sidebar.number_input("Fin del Dominio", value=10, step=1)
    
    if start > end:
        st.sidebar.error("⚠️ El inicio debe ser menor o igual al fin.")
        domain = []
    else:
        domain = get_domain(start, end)
    
    st.subheader("📊 Dominio de Evaluación")
    st.write(f"**Dominio:** {domain}")
    
    st.subheader("🔍 Evaluación de P(x)")
    results = {x: P(x) for x in domain}
    for x, result in results.items():
        color = "🟢 Verdadero" if result else "🔴 Falso"
        st.write(f"P({x}) = {color}")
    
    st.subheader("🧮 Evaluar Proposiciones Cuantificadas")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ ∀x ∈ dominio, P(x)"):
            if not domain:
                st.warning("Define un dominio válido primero.")
            else:
                result = forall(domain, P)
                if result:
                    st.success("La proposición ∀x ∈ dominio, P(x) es **VERDADERA**.")
                else:
                    st.error("La proposición ∀x ∈ dominio, P(x) es **FALSA**.")
    
    with col2:
        if st.button("✅ ∃x ∈ dominio, P(x)"):
            if not domain:
                st.warning("Define un dominio válido primero.")
            else:
                result = exists(domain, P)
                if result:
                    st.success("La proposición ∃x ∈ dominio, P(x) es **VERDADERA**.")
                else:
                    st.error("La proposición ∃x ∈ dominio, P(x) es **FALSA**.")

if __name__ == "__main__":
    main()
