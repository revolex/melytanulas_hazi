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
## Related works
- Related GitHub repositories:
    - https://huggingface.co/blog/annotated-diffusion
    - https://github.com/huggingface/diffusers
    - https://keras.io/examples/generative/ddim/

- Related papers:
    - https://arxiv.org/abs/2006.11239
    - https://arxiv.org/abs/2010.02502

## How to run
1. docker buildx build -t <image_name> .
2. docker run -v ${PWD}/data:/root -it <image_name>

