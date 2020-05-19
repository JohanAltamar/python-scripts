import sqlite3

conn = sqlite3.connect("SSAM.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (usuario_id text NOT NULL, password text NOT NULL)''')
# c.execute('DELETE FROM usuarios')
def create_user ():
    c = conn.cursor()
    user = input('Ingrese usuario: ').lower()
    check_username(user)
    contr = input('Ingrese contrasena: ')
    usuario_nuevo=(user,contr)
    c.executemany("INSERT INTO usuarios VALUES (?,?)",(usuario_nuevo,))
    conn.commit()
    conn.close()

def check_username(user):
    c.execute('SELECT usuario_id FROM usuarios')
    names = {name[0] for name in c.fetchall()}
    if user in names:
        print ("Usuario ya existe. Ingrese nuevamente.")
        create_user()

def find_username():
    t=input('Ingrese usuario para la busqueda: ')
    c.execute('SELECT * FROM usuarios WHERE usuario_id=?', (t,))
    print (c.fetchone())

def validation():
    c = conn.cursor()
    user = input('Ingrese usuario: ').lower()
    contr = input('Ingrese contrasena: ')
    c.execute('SELECT usuario_id, password FROM usuarios WHERE usuario_id = ? AND password = ?',(user, contr) )
    names = {name[0] for name in c.fetchall()}
    if user in names:
        print ("Ingreso exitoso.")
    else:
        print("Usuario y/o contrasena no son correctos. Ingrese nuevamente")
        validation()
    # conn.commit()
    # conn.close()

#Uncomment option selected and execute
#find_username()
#create_user()
validation()
