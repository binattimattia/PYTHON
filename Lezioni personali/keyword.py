print(1, 2, 3, 4, 5, sep="-")   # sep è utile per separare dati e riconosce in automatico quando non va messo

def ottieni_numero(paese, area, primi, ultimi):
    return f"+{paese} {area}-{primi}-{ultimi}"

print(ottieni_numero(paese=39, area=344, primi=286, ultimi=6778))  # non è necessario specificare il parametro
