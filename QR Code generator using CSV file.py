import pandas as pd
import qrcode
from PIL import Image

# Load your CSV file into a DataFrame (adjust the file path if needed)
csv_file = 'C:/Users/HP/Downloads/protik bhai.csv'

df = pd.read_csv(csv_file)

# Loop through each row of the dataframe to create QR codes
for index, row in df.iterrows():
    # Assuming you want to generate a QR code from the first column data
    data = row[0]  # Change the column index or name as needed (e.g., row['column_name'])

    # Create the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box
        border=4,  # Size of the border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image with a unique name (e.g., based on the row index)
    img.save(f"qr_code_{index + 1}.png")

    print(f"QR code for row {index + 1} saved as qr_code_{index + 1}.png")
