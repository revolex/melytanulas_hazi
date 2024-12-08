## Csapatnév: 
Nem tudjuk mi volt, nem érkezett visszajelzés a formról és nem tudjuk visszanézni se.
## Csapattagok:
- Safár Gergő / LM1ZJR
- Köpeczi-Bócz Gergely / HL7KTX
## Projekt leírás:
Image generation with diffusion models

Implement and train unconditional diffusion models, such as DDPM (Denoising Diffusion Probabilistic Model) or DDIM (Denoising Diffusion Implicit Model) for generating realistic images. Evaluate the capabilities of the models on two different datasets, such as CelebA and Flowers102.
## Fájlok
- ./data : Ide kerülnek letöltés után a datasetek.
- Dockerfile: Ennek a futtatásával buildelhető a konténer
- image_gen.ipynb: Ebben található az első milestonenal kapcsolatos python kód, illetve a datasetekhez kapcsolódó analízis is.
- requirements.txt: Ez tartalmazza a Dockerfile buildelése során behúzandó könyvtárakat, amik kellenek a model működéséhez.
- README.md: Ez a fájl :)
- service.py: ML as service implementáció, lehet kérni tőle képeket
- supervisord.conf: Dockerhez hogy automatikusan indítsa a notebook szervert és a service-t.
- frontend.html: Frontend UI képek generálásához
## Related works
- Related GitHub repositories:
    - https://huggingface.co/blog/annotated-diffusion
    - https://github.com/huggingface/diffusers
    - https://keras.io/examples/generative/ddim/

- Related papers:
    - https://arxiv.org/abs/2006.11239
    - https://arxiv.org/abs/2010.02502

## How to run
1. docker build -t melytanulas_hazi .
2. docker run --gpus all -p 8888:8888 melytanulas_hazi
3. open in a browser: http://127.0.0.1:8888/tree?token=XXXXXXX... (it will show up in the terminal after the run command)
4. open and Run all in the image_gen.ipynb file
5. The model training, its evaluation and the comparison of both models will be found in the notebook once the run has finished.

## How to use service
1. Run all in the notebook
2. Install everything in requirements.txt, if not in docker container
3. If docker container is launched, then it's accessible on localhost:6565/generate-pet or /generate-flower
4. If you are not using docker container you can start it without docker, with python3 service.py
5. Open frontend.html in your browser and enjoy the pictures
