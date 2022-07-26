
from functools import wraps

def decorala(func):
    @wraps(func)
    def stampa_nome(*arg, **keyw):
        """stampa il nome della funzione"""
        print("a richiesta di enrico eseguo ", func.__name__)
        ret = func(*arg, **keyw)
        return ret
    
    return stampa_nome

@decorala
def pippo():
    """saluta pippo"""
    print("ciao Pippo")

pippo()
print(pippo.__doc__)
