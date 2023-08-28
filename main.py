import json 

from models.pross_json_entrada import ManipulandoJson
from models.crop import CropImg

mj = ManipulandoJson()
crop_img = CropImg()
with open('Frisa/camera_externa.json', 'r') as arquivo:
    dados = json.load(arquivo)

bundbox = mj.get_bundbox(dados)
rotation = mj.get_rotation(dados)
crop_img.salve_crop(bundbox, rotation)
