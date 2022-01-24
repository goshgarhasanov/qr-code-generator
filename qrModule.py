import qrcode
import image
def create_QR(txt="myText",img_name="myimage"):
    qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
    qr.add_data(txt)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save(img_name+".png")

    print(img)

