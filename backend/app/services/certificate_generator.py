import os
from datetime import datetime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


BASE = "app/static"


def center(draw, text, font, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    return (width - text_width) // 2


def generate_certificate(
    uuid,
    fullname,
    course,
    trainer,
    background,
    qr_path
):

    # ==========================
    # Background
    # ==========================

    bg = Image.open(
        os.path.join(
            BASE,
            "backgrounds",
            background
        )
    ).convert("RGB")

    bg = bg.resize((1600, 1131))

    draw = ImageDraw.Draw(bg)

    # ==========================
    # Gold Border
    # ==========================

    draw.rectangle(
        (20, 20, 1580, 1111),
        outline="#D4AF37",
        width=8
    )

    draw.rectangle(
        (45, 45, 1555, 1086),
        outline="#D4AF37",
        width=2
    )

    # ==========================
    # Fonts
    # ==========================

    title_font = ImageFont.truetype(
        os.path.join(BASE, "fonts", "Poppins-Bold.ttf"),
        70
    )

    name_font = ImageFont.truetype(
        os.path.join(BASE, "fonts", "Poppins-Bold.ttf"),
        85
    )

    text_font = ImageFont.truetype(
        os.path.join(BASE, "fonts", "Poppins-Regular.ttf"),
        36
    )

    small_font = ImageFont.truetype(
        os.path.join(BASE, "fonts", "Poppins-Regular.ttf"),
        22
    )

    # ==========================
    # Logo
    # ==========================

    logo_path = os.path.join(BASE, "logos", "logo.png")

    if os.path.exists(logo_path):

        logo = Image.open(logo_path).convert("RGBA")

        logo = logo.resize((150, 150))

        bg.paste(
            logo,
            (70, 60),
            logo
        )

    # ==========================
    # Title
    # ==========================

    width = bg.size[0]

    draw.text(
        (
            center(
                draw,
                "CERTIFICATE OF COMPLETION",
                title_font,
                width
            ),
            120
        ),
        "CERTIFICATE OF COMPLETION",
        fill="#1e293b",
        font=title_font
    )

    # ==========================
    # Subtitle
    # ==========================

    draw.text(
        (
            center(
                draw,
                "This Certificate is Proudly Presented To",
                text_font,
                width
            ),
            240
        ),
        "This Certificate is Proudly Presented To",
        fill="#444444",
        font=text_font
    )

    # ==========================
    # Full Name
    # ==========================

    draw.text(
        (
            center(
                draw,
                fullname,
                name_font,
                width
            ),
            330
        ),
        fullname,
        fill="#1d4ed8",
        font=name_font
    )

    # ==========================
    # Description
    # ==========================

    description = (
        f"For successfully completing the course "
        f"\"{course}\""
    )

    draw.text(
        (
            center(
                draw,
                description,
                text_font,
                width
            ),
            470
        ),
        description,
        fill="#222222",
        font=text_font
    )

    # ==========================
    # Trainer
    # ==========================

    draw.text(
        (
            center(
                draw,
                f"Instructor : {trainer}",
                text_font,
                width
            ),
            540
        ),
        f"Instructor : {trainer}",
        fill="#222222",
        font=text_font
    )

    # ==========================
    # Date
    # ==========================

    today = datetime.now().strftime("%d.%m.%Y")

    draw.text(
        (1120, 760),
        f"Date : {today}",
        fill="#333333",
        font=text_font
    )

    # ==========================
    # Signature
    # ==========================

    draw.line(
        (180, 860, 520, 860),
        fill="#000000",
        width=2
    )

    draw.text(
        (220, 875),
        "Instructor Signature",
        fill="#444444",
        font=small_font
    )

    # ==========================
    # QR Code
    # ==========================

    qr = Image.open(qr_path)

    qr = qr.resize((180, 180))

    bg.paste(
        qr,
        (1320, 820)
    )

    draw.text(
        (1335, 1015),
        "Scan to Verify",
        fill="#444444",
        font=small_font
    )

    # ==========================
    # UUID
    # ==========================

    draw.text(
        (60, 1015),
        f"UUID : {uuid}",
        fill="#666666",
        font=small_font
    )

    # ==========================
    # Verify URL
    # ==========================

    verify = f"http://127.0.0.1:8000/verify/{uuid}"

    draw.text(
        (60, 1050),
        verify,
        fill="#666666",
        font=small_font
    )

    # ==========================
    # Save
    # ==========================

    os.makedirs(
        os.path.join(BASE, "certificates"),
        exist_ok=True
    )

    output = os.path.join(
        BASE,
        "certificates",
        f"{uuid}.png"
    )

    bg.save(
        output,
        quality=100
    )

    return output