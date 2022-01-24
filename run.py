import qrModule
import time

while True:
    try:
        txt, img_name = input("""
    ---------  QR CODE CREATOR ------------
    -  /// DEVELOPMENT BY GOSHGAR HASANOV ///
    -
    -QR CODE YARATMAQ ÜÇÜN  Mətn adını və
    - Şəkil ad və formatını daxil edin
    -Nümunə: hasanov/qrimageName
    -Heçnə daxil etməsəniz default olaraq
    -yaradılacaq və myText myimage.png 
    -olaraq adlandırılacaq
    ---------  QR CODE CREATOR ------------
    >>> """).split('/')
        qrModule.create_QR(txt=txt,img_name=img_name)
        break

    except ValueError:
        print("""Xahiş edirik 
        Mətni və Şəkil adını Nümunəyə uyğun daxil edəsiniz
        """)
        time.sleep(5)
