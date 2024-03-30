import qrcode
import os 

data = input() # The data you want to encode into the QR code
folder_path = "D:/CODE_LEARN_CODE_BLOCK/PYTHON/multi_able_lib/qr gen/anh_qr"  # The path to save the QR code image file

if not os.path.exists(folder_path):
    os.makedirs(folder_path)  
    
    
# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")



file_name = input()
file_path = os.path.join(folder_path, file_name)
# Save the image file
qr_image.save(file_path)