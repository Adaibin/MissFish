import qrcode

__author__ = 'Mr Fish.'


qr = qrcode.QRCode(version=7,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=30)

qr.add_data('https://cn.vuejs.org/v2/guide/')
qr.make()
img = qr.make_image(fill_color="white", back_color="blue")
img.save(open('vue.png', 'wb'))
