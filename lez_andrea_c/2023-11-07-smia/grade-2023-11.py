# -*- coding: utf-8 -*-
import testlib
import os
import glob
import sys
import filecmp

# if not os.path.isfile('program.py'): # questo non funziona se la working directory cambia, come accade nel mio caso 
program_pathname = os.path.join("lez_andrea_C","2023-11-07-smia","program.py")
if not os.path.isfile(program_pathname): # questo non funziona se la working directory cambia, come accade nel mio caso 
    print('WARNING: Save program_smia.py as program.py\n'
          'ATTENZIONE: salvare program_smia.py con nome program.py')
    sys.exit(0)

import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#############################################################################

def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)

def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################

def eqfiles(f, g):
    file1 = open(f, 'r')
    file2 = open(g, 'r')

    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

    if(len(file1_lines) != len(file2_lines)):
        file1.close()
        file2.close()
        return False

    for i in range(len(file1_lines)):
        if file1_lines[i].replace("\r\n", "\n") != file2_lines[i].replace("\r\n", "\n"):
            file1.close()
            file2.close()
            return False
    file1.close()
    file2.close()
    return True

# ----------------------------------- Esercizio 1 ----------------------------------- #
def do_ex1_tests(input, expected_out): 
    d = program.ex1(input)
    if d != expected_out:
        print(f'''{'*'*50}\n[ERROR] Il risultato deve essere \n{expected_out} anziché \n{d}.\n{'*'*50}''')
        return 0        # test non passato
    return 1            # test passato (1 punto)


def test_ex1_1():
    input = ['radar','ada']
    out = {'ada': (set(), 0), 'radar': (set(), 0)}
    return do_ex1_tests(input, out)

def test_ex1_2():
    input = ['banana','ananab','anana','naana','annaa','2552']
    out = {'ananab': (set(['banana']), 1), 'annaa': (set(['anana', 'naana']), 2), '2552': (set(), 0)}
    return do_ex1_tests(input, out)

def test_ex1_3():
    input = ['radar', 'ardra']
    out = {'ardra': (set(['radar']), 1)}
    return do_ex1_tests(input, out)



# ----------------------------------- Esercizio 2 ----------------------------------- #
def do_ex2_tests(input, expected_out):    
    d = program.ex2(input)
    if d != expected_out:
        print(f'''{'*'*50}\n[ERROR] Il risultato deve essere {expected_out} anziché {d}.\n{'*'*50}''')
        return 0
    return 1


def test_ex2_1():
    input = ['radar','ada']
    out = {'radar': (set(['ada']), 1)}
    return do_ex2_tests(input, out)

def test_ex2_2():
    input = ['banana','ananab','anana','naana','annaa','2552']
    out = {'annaa': (set(), 0), 'banana': (set(['anana']), 1), 'ananab': (set(['anana']), 1), 'naana': (set(), 0), '2552': (set(), 0)}
    return do_ex2_tests(input, out)

def test_ex2_3():
    input = set(['pino', ''])
    out = {'pino': (set(['']), 1)}
    return do_ex2_tests(input, out)


# ----------------------------------- Esercizio 3 ----------------------------------- #
def do_ex3_tests(input, expected_out):    
    d = program.ex3(input)
    if d != expected_out:
        print(f'''{'*'*50}\n[ERROR] Il risultato deve essere {expected_out} anziché {d}.\n{'*'*50}''')
        return 0
    return 1


def test_ex3_1():
    input = ['radar','ada']
    out =  {True: (set(['ada', 'radar']), 2), False: (set(), 0)}
    return do_ex3_tests(input, out)

def test_ex3_2():
    input = ['banana','ananab','anana','naana','annaa','2552']
    out = {True: (set(['anana', '2552']), 2), False: (set(['annaa', 'banana', 'ananab', 'naana']), 4)}
    return do_ex3_tests(input, out)

def test_ex3_3():
    input = ['']
    out = {True: (set(['']), 1), False: (set(), 0)}
    return do_ex3_tests(input, out)


###############################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex1_1, test_ex1_2, test_ex1_3, 
    test_ex2_1, test_ex2_2, test_ex2_3, 
    test_ex3_1, test_ex3_2, test_ex3_3, 
    test_personal_data_entry,
]
###############################################################################

###############################################################################
#
# Qui i test segreti
#

f = "test-segreti-2023-11.py"
if os.path.isfile(f):       # lancia i test segreti se il file esiste
    exec(open(f).read())
    tests += test_segreti   # test_segreti e' definita dal file appena eseguito
    
###############################################################################


###############################################################################
if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv')
################################################################################