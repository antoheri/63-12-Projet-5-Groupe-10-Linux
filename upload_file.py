from ftplib import FTP
# connection parameters
def upload_file(filename, HOST, USERNAME, PASSWORD):
    host = HOST
    user = USERNAME
    password = PASSWORD

    ftp = FTP()
    ftp.connect(host)
    ftp.login(user, password)

    ftp.cwd("log")

    with open(filename, 'rb') as file:
        ftp.storbinary(f"STOR {filename}", file)
        ftp.quit()
