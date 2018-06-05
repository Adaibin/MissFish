import qrcode

__author__ = 'Mr Fish.'


qr = qrcode.QRCode(version=7,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=30)

qr.add_data('http://miss-fish.com/dairy/flask.html')
qr.make()
img = qr.make_image(fill_color="black", back_color="white")
img.save(open('flask.png', 'wb'))
