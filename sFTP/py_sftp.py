import pysftp as sftp
import os
import shutil
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0




def upload_file(conn, source_dir, dest_dir, fname, verbose = True):
    try:
        conn.cwd(remote_dir)
        fpathname = os.path.join(source_dir,fname)
        if verbose:
            print(f'uploading {fpathname}')
        conn.put(fpathname)
        return True
    except Exception as e:
        print(e)
        return False


def upload_files(source_dir, dest_dir, dir_inviati):

    with sftp.Connection(host=host, username=user, password=password,log=log_file, port = port, cnopts=cnopts) as sftp_conn:
        sftp_conn.cwd(remote_dir)  # The full path 
        print("working directory", sftp_conn.getcwd())
        # get files list
        fnames_list = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
        print(f'trovati {len(fnames_list)} files da inviare in {source_dir}')
        for fname in fnames_list:
            ok = upload_file(sftp_conn, source_dir, dest_dir, fname)
            if ok:
                shutil.move(os.path.join(source_dir,fname),dir_inviati)
        else:
            print("#"*10+" upload file terminato correttamente"+"#"*10)



ini_file = "./sFTP/sftp.ini"

config = ConfigParser() # instantiate
ok = config.read(ini_file) # parse existing file
if len(config.sections()) <= 0:
    print(f'ERRORE: config file vuoto o non trovato\nfile: {ini_file}\nworking dir: {os.getcwd()}')
    exit(1)

print(f'working directory: {os.getcwd()}')
host = string_val = config.get('remotehost', 'host').strip()
port =  string_val = int(config.get('remotehost', 'port').strip())
user = config.get('remotehost', 'user').strip()
password = config.get('remotehost', 'password').strip()
remote_dir = config.get('remotehost', 'remote_dir').strip()

local_source_dir = config.get('localhost', 'local_source_dir').strip()
log_file = config.get('localhost', 'script_log_file').strip()



# evita un bug interno
cnopts = sftp.CnOpts()
cnopts.hostkeys = None

if not os.path.isdir(local_source_dir):
    print(f'non trovata directory sorgente: {local_source_dir}')
    exit(1)

dir_inviati = os.path.join(local_source_dir,"inviati")
if not os.path.isdir(dir_inviati):
    os.mkdir(dir_inviati)
upload_files(local_source_dir, remote_dir, dir_inviati)
