# Multiple Image Cropper

> Este projeto permite realizar múltiplos cortes em uma ou várias imagens de uma só vez com base em coordenadas fornecidas no formato YOLO.

## Instalação

1. Clone este repositório:

```bash
git clone git@github.com:LuanAccioly/multiple-image-cropper.git
```

2. Dentro do repositório, crie e ative o ambiente virtual:

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

3. Instale as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Uso

1. As imagens completas devem ser colocadas na pasta `contents/full_images`.
2. As coordenadas YOLO para os cortes devem ser fornecidas na pasta `content/yolo_coordinates/questions`. Cada arquivo de coordenadas deve corresponder a uma imagem (ter o mesmo nome) na pasta `full_images`.
3. Execute o script principal `main.py` para realizar os cortes:

```bash
python main.py
```

4. As imagens cortadas serão salvas na pasta `content/cropped_questions`.