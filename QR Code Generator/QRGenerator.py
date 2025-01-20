'''
This code is about genrating qr code based on the input text given
for eg if the user enters "www.google.com", it creates a qr code based on that text given
and saves the qr code in the same directory as the python file with the png name provided by the user entered
'''

import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)
    print(f"QR Code saved to {filename}")

if __name__ == "__main__":
    input_data = input("Enter data to be written in QR Code: ")
    filename = input("Enter filename to save the QR Code (along with extension (PNG): ")
    generate_qr_code(input_data, filename)

