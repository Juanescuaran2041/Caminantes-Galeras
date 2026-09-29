"""Ensambla la OVA: incrusta imágenes y videos de /media en src/index.template.html
y genera caminantes-del-galeras.html (un solo archivo autocontenido)."""
import base64, json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
M = os.path.join(ROOT, 'media')
img = {f[:-4]: 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(M, f), 'rb').read()).decode()
       for f in sorted(os.listdir(M)) if f.endswith('.jpg')}
vid = {f[:-4]: base64.b64encode(open(os.path.join(M, f), 'rb').read()).decode()
       for f in sorted(os.listdir(M)) if f.endswith('.mp4')}
assets = 'const IMG = ' + json.dumps(img) + ';\nconst VID = ' + json.dumps(vid) + ';'
html = open(os.path.join(ROOT, 'src', 'index.template.html'), encoding='utf-8').read().replace('/*__ASSETS__*/', assets)
out = os.path.join(ROOT, 'caminantes-del-galeras.html')
open(out, 'w', encoding='utf-8').write(html)
print(f'Listo: {out} ({len(html)/1e6:.1f} MB)')
