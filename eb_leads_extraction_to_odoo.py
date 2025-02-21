import importlib

# Lista de módulos a ejecutar
modules = [
    "src.extraction.eb_leads",
    "src.manipulation.eb_leads",
    "src.update.eb_leads"
]

def run_module(module_name):
    """Importa y ejecuta un módulo dinámicamente."""
    print(f"🔄 Ejecutando módulo: {module_name}")
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "main"):
            module.main()  # Llamar a la función `main()` si existe
        else:
            print(f"⚠️ El módulo {module_name} no tiene una función `main()`, solo se ha importado.")
    except Exception as e:
        print(f"❌ Error al ejecutar {module_name}: {e}")
        return e

if __name__ == "__main__":
    for mod in modules:
        result = None
        result = run_module(mod)
        if result:
            break


