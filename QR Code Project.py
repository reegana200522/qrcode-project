import qrcode

print("===== QR CODE GENERATOR =====")

# Get input from user
data = input("Enter text or URL: ")

# Check input
if data.strip() == "":
    print("Please enter valid text or URL.")

else:
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create QR Code image
    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Save QR Code
    img.save("my_qrcode.png")

    print("QR Code generated successfully!")
    print("Saved as my_qrcode.png")
