import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = '6.OR코드생성기\\' + qr_data + '.png'

qr_img.save(save_path)