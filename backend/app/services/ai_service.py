import os
import uuid
import torch

from diffusers import FluxPipeline

MODEL_PATH = "./models/flux"

pipe = None


def load_model():

    global pipe

    if pipe is None:

        pipe = FluxPipeline.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float16
        )

        pipe.enable_model_cpu_offload()

    return pipe


def generate_background(prompt: str):

    os.makedirs("app/static/backgrounds/generated", exist_ok=True)

    pipeline = load_model()

    image = pipeline(
        prompt,
        guidance_scale=3.5,
        num_inference_steps=4,
        height=768,
        width=1152
    ).images[0]

    filename = f"{uuid.uuid4()}.png"

    filepath = os.path.join(
        "app/static/backgrounds/generated",
        filename
    )

    image.save(filepath)

    return filepath