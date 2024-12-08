from flask import Flask, jsonify, send_file
from io import BytesIO
from PIL import Image
import numpy as np
from diffusers import DDPMPipeline
import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

output_dir_f = "./trained_model_flowers" 
output_dir_p = "./trained_model_pets" 

pipeline_flowers = DDPMPipeline.from_pretrained(output_dir_f)
pipeline_pets = DDPMPipeline.from_pretrained(output_dir_p)


device = "cuda" if torch.cuda.is_available() else "cpu"
pipeline_flowers.to(device)
pipeline_pets.to(device)


num_images = 5 
num_inference_steps = 50 
generator = torch.manual_seed(42)


@app.route('/generate-pet', methods=['GET'])
def generate_image_pet():
    img = pipeline_pets(
        num_inference_steps=num_inference_steps,
        generator=generator
    ).images[0]

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

@app.route('/generate-flower', methods=['GET'])
def generate_image_flower():
    img = pipeline_flowers(
        num_inference_steps=num_inference_steps,
        generator=generator
    ).images[0]
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6565)
