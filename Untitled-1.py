from functools import wraps

def agente_d(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[INFORME]: ¡Agente D infiltrando al objetivo '{func.__name__}'!")
        print(f"[INTELIGENCIA]: Equipamiento táctico (args) detectado: {args}")
        print(f"[INTELIGENCIA]: Documentos secretos (kwargs) recuperados: {kwargs}")

        resultado = func(*args, **kwargs)

        print(f"[EXTRACCIÓN]: ¡Misión cumplida! El objetivo ha revelado el secreto: {resultado!r}")
        return resultado
    return wrapper


@agente_d
def desactivar_bomba(codigo, tiempo_restante=60):
    return "Bomba desactivada con éxito."

desactivar_bomba("código-azul", tiempo_restante=30)