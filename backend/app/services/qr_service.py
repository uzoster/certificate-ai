import os
import qrcode


def generate_qr(uuid: str):

    os.makedirs("app/static/qrcodes", exist_ok=True)

    verify_url = f"http://localhost:5173/verify/{uuid}"

    filename = f"{uuid}.png"

    filepath = os.path.join(
        "app/static/qrcodes",
        filename
    )

    img = qrcode.make(verify_url)

    img.save(filepath)

    return filepath