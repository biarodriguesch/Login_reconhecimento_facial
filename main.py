import io
import cv2
import sqlite3
import numpy as np
import face_recognition

from time import sleep
from threading import Thread
from sqlite3 import Error
from PIL import Image, ImageTk, UnidentifiedImageError

from front.interface import Interface

class MenuPrincipal(Interface):
    def _conecxao_db(page):
        try:
            return sqlite3.connect("database/pessoas.db", detect_types = sqlite3.PARSE_DECLTYPES)
        except sqlite3.OperationalError:
            from os import mkdir
            mkdir('database')
        finally:
            return sqlite3.connect("database/pessoas.db", detect_types = sqlite3.PARSE_DECLTYPES)

    def _tabela_registros_existe(page, cur):
        return not(cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='registros';""").fetchall() == [])

    def _adaptar_array(page, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def _converter_array(page, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def _webcam_durante_registro(page):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)        

        def mostrar_webcam():
            page._criar_frame_webcam()

            try:
                while True:
                    _, page.captura_webcam = cap.read()
                    page.captura_webcam = cv2.flip(page.captura_webcam, 1)
                    page.captura_webcam = cv2.resize(page.captura_webcam, (430, 350)) 
                    cv2image = cv2.cvtColor(page.captura_webcam, cv2.COLOR_BGR2RGBA)
                    img = Image.fromarray(cv2image)
                    imgtk = ImageTk.PhotoImage(image = img)

                    if page.webcam_frame.winfo_exists():
                        page.webcam_frame.imgtk = imgtk
                        page.webcam_frame.configure(image = imgtk)
                    else: 
                        break

                    if page.continuar_mostrando_webcam:
                        sleep(0.01) 
                        cv2.destroyAllWindows()
                        while not page.continuar_mostrando_webcam:
                            sleep(0.005)
                            
            except cv2.error:
                page._tela_de_aviso("Ocorreu um erro!\nSua webcam não está disponível.")
                page.frame_registro.destroy()

        page.thread1 = Thread(target = mostrar_webcam, daemon = True)
        page.thread1.start()

    def _botao_login_clicado(page):
        sqlite3.register_converter("array", page._converter_array) 
     
        conn = page._conecxao_db()
        cur = conn.cursor()

        if page._tabela_registros_existe(cur):
            page._criar_interface_login()

            Thread(target = page._login_webcam, daemon = True).start()
            Thread(target = page._login_validacao, args = (cur.execute("SELECT * FROM registros").fetchall(), ), daemon = True).start()  
        else:
            page._tela_de_aviso("Não há ninguém registrado no momento!")                           

        conn.close()

    def _login_webcam(page):
        trained_data = cv2.CascadeClassifier('./frontal-face-data.xml')
        webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        page._criar_frame_webcam()

        def mostrar_webcam():
            try:
                _, page.captura_webcam = webcam.read()
                page.captura_webcam = cv2.flip(page.captura_webcam, 1)
                page.captura_webcam = cv2.resize(page.captura_webcam, (430, 350))

                for (x, y, w, h) in trained_data.detectMultiScale(cv2.cvtColor(page.captura_webcam, cv2.COLOR_BGR2GRAY)):
                    cv2.rectangle(page.captura_webcam, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                imgtk = ImageTk.PhotoImage(image = Image.fromarray(cv2.cvtColor(page.captura_webcam, cv2.COLOR_BGR2RGBA)))
                page.webcam_frame.imgtk = imgtk
                page.webcam_frame.configure(image = imgtk)
                page.webcam_frame.after(10, mostrar_webcam)
            except (TypeError, cv2.error):
                pass 
        mostrar_webcam()

    def _login_validacao(page, pessoas):
        def atualizar_texto_validando():
            while page.continuar_atualizando_texto:
                for i in range(4):
                    if page.continuar_atualizando_texto:
                        page.texto_validando.configure(text = "VALIDANDO" + ('.' * i))
                        sleep(0.5)
                    else:
                        break

        while True:
            t = Thread(target = atualizar_texto_validando)
            try:
                encoding_desconhecida = face_recognition.face_encodings(page.captura_webcam)[0]

                page.texto_validando.place(relx = 0.439, rely = 0.867, height = 19, width = 200)
                page.continuar_atualizando_texto = True
                t.start()
                
                for registrado in pessoas:
                    encoding_img_registrada = face_recognition.face_encodings(registrado[2])[0]
                    resultado = face_recognition.compare_faces([encoding_img_registrada], encoding_desconhecida, tolerance = 0.6)
                    
                    if resultado[0]:
                        sleep(2)
                        cv2.destroyAllWindows()
                        page.continuar_atualizando_texto = False  
                        page.frame_feed_webcam.destroy()
                        page._exibir_dados_confidenciais(registrado[0], registrado[1])
                        break
                
                if resultado[0]:
                    break
                else:
                    page.continuar_atualizando_texto = False
                    page.texto_validando.place(relx=0.285, rely=0.867, height=19, width=300)
                    page.texto_validando.configure(text="Você não está cadastrado neste banco de dados.")
                    sleep(2)

            except (IndexError, FileNotFoundError, UnidentifiedImageError):
                if page.frame_login.winfo_exists():
                    page.texto_validando.place(relx=0.325, rely=0.867, height=19, width=200)
                    page.texto_validando.configure(text="Não foi possível identificar uma face.")
                    sleep(2) 
            except TypeError:
                page.frame_login.destroy()
                page._tela_de_aviso("Ocorreu um erro!\nSua webcam não está disponível.")
                break
            except AttributeError:
                sleep(0.3)

    def _salvar_database(page, nome, cargo):
        def ja_cadastrado(pessoas):
            try:
                encoding_desconhecida = face_recognition.face_encodings(page.captura_webcam)[0]

                for registrado in pessoas:
                    encoding_img_registrada = face_recognition.face_encodings(registrado[2])[0]
                    resultado = face_recognition.compare_faces([encoding_img_registrada], encoding_desconhecida, tolerance = 0.6)
                    
                    if resultado[0]:
                        return 1
                return 0
            except (IndexError, FileNotFoundError, UnidentifiedImageError):
                return -1

        sqlite3.register_converter("array", page._converter_array)
        sqlite3.register_adapter(np.ndarray, page._adaptar_array)

        conn = page._conecxao_db() 
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS registros (nome text, cargo int, arr array)")

        temp = ja_cadastrado(cur.execute("SELECT * FROM registros").fetchall())
        if temp == 1:
            page._tela_de_aviso("Você já está registrado neste programa.")
            page.continuar_mostrando_webcam = True
            page.botao_confirmar_registro.lower()
        elif temp == 0:         
            cur.execute("INSERT INTO registros (nome, cargo, arr) VALUES (?, ?, ?)", (nome, cargo, page.captura_webcam, ))
            conn.commit()
            page.thread1.join(0.001)
            page.frame_registro.destroy()
            page._tela_de_aviso("Você foi registrado com sucesso!")
        elif temp == -1:
            page._tela_de_aviso("Nenhum rosto foi detectado na imagem.")
            page.continuar_mostrando_webcam = True
            page.botao_confirmar_registro.lower()
            
        conn.close()

if __name__ == "__main__":
    MenuPrincipal()