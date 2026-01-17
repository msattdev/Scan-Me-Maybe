import qrcode
from PIL import Image, ImageDraw
from ascii_art import LOGO

def round_corners(image, radius=20):
    """Add rounded corners to an image"""
    # Create a mask with rounded corners
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    
    # Apply the mask to the image
    output = Image.new('RGBA', image.size, (0, 0, 0, 0))
    output.paste(image, (0, 0))
    output.putalpha(mask)
    return output

def generate_qr_code(data, filename, fill_color="black", back_color="white", box_size=10, border=2):
    """Generate a QR code with rounded corners"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    
    # Add rounded corners
    img = round_corners(img, radius=15)
    
    img.save(filename)
    return img

def generate_styled_qr_code(data, filename, fill_color="#1F51BA", back_color="#FFFFFF"):
    """Generate a modern styled QR code with rounded corners and padding"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    
    # Add rounded corners
    img = round_corners(img, radius=20)
    
    # Add elegant padding/border for modern look
    padding = 30
    new_size = (img.size[0] + 2*padding, img.size[1] + 2*padding)
    new_img = Image.new('RGBA', new_size, (255, 255, 255, 0))
    new_img.paste(img, (padding, padding), img)
    
    new_img.save(filename)
    return new_img

if __name__ == "__main__":
    print(LOGO)
    print("-" * 40)
    
    qr_data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter filename (default: qrcode.png): ").strip() or "qrcode.png"
    
    style = input("Choose style (1=Classic, 2=Modern Blue): ").strip() or "1"
    
    if style == "2":
        generate_styled_qr_code(qr_data, filename)
        print(f"Modern QR code with rounded edges generated and saved as {filename}")
    else:
        generate_qr_code(qr_data, filename)
        print(f"QR code with rounded edges generated and saved as {filename}")
