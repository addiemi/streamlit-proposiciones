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
    
    # Título Principal
    st.title("📚 Funciones Proposicionales y Cuantificadores")
    
    # Sección de Instrucciones y Propósito
    st.header("🔍 ¿Para Qué Sirve Esta Aplicación?")
    st.markdown("""
    Esta aplicación te permite **identificar números pares** dentro de un rango definido y **evaluar proposiciones** utilizando cuantificadores universales y existenciales.
    
    ### 📋 **Objetivos de la Aplicación**
    - **Identificar Números Pares**: Ingresa un rango de números y la aplicación mostrará cuáles son pares.
    - **Evaluar Proposiciones Cuantificadas**:
      - **Universal (∀)**: "Todos los números en el dominio son pares."
      - **Existencial (∃)**: "Existe al menos un número par en el dominio."
    
    ### 🛠️ **Cómo Usar la Aplicación**
    1. **Definir el Dominio**:
       - En la barra lateral, ingresa el **número de inicio** y el **número de fin** para definir el rango de números que deseas evaluar.
    2. **Visualizar el Dominio**:
       - La aplicación mostrará el dominio actual en la sección "📊 Dominio de Evaluación".
    3. **Evaluar P(x)**:
       - La sección "🔍 Evaluación de P(x)" mostrará cuáles números en el dominio son pares (**Verdadero**) o impares (**Falso**).
    4. **Evaluar Proposiciones Cuantificadas**:
       - **∀x ∈ dominio, P(x)**: Haz clic en este botón para verificar si **todos** los números en el dominio son pares.
       - **∃x ∈ dominio, P(x)**: Haz clic en este botón para verificar si **al menos uno** de los números en el dominio es par.
    """)

    # Barra Lateral para Configuración del Dominio
    st.sidebar.header("🔧 Configuración del Dominio")
    
    start = st.sidebar.number_input("Inicio del Dominio", value=1, step=1)
    end = st.sidebar.number_input("Fin del Dominio", value=10, step=1)
    
    if start > end:
        st.sidebar.error("⚠️ El inicio debe ser menor o igual al fin.")
        domain = []
    else:
        domain = get_domain(start, end)
    
    # Mostrar el Dominio de Evaluación
    st.subheader("📊 Dominio de Evaluación")
    st.write(f"**Dominio:** {domain}")
    
    # Evaluación de P(x)
    st.subheader("🔍 Evaluación de P(x)")
    results = {x: P(x) for x in domain}
    for x, result in results.items():
        color = "🟢 Verdadero" if result else "🔴 Falso"
        st.write(f"P({x}) = {color}")
    
    # Evaluar Proposiciones Cuantificadas
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

