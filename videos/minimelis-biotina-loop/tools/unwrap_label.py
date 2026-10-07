"""Unwrap the front of the bottle label from the upright reference photo.

Pinhole model fitted to the label's curved bottom edge: the bottle axis is
vertical at x=CX, the camera sits at the height of the label top, D radii
from the axis, focal length F px. A label point at angle theta (0 = facing
camera) and height fraction v (of H radii) projects to
  x = CX + F*sin(theta)/(D - cos(theta))
  y = TOP + F*v*H/(D - cos(theta))
Baked shading is flattened with a per-column white reference taken from the
blank strip just under the label top edge.
"""
import sys, math
import numpy as np
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
img = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
CX, TOP = 1006.0, 733.0
D, F, H = 8.45, 3196.8, 2.194   # radii, px, radii
TH = math.radians(80)          # unwrap +-80 degrees (silhouette is at 83.2)
OUT_H = 1536
OUT_W = int(round(OUT_H * 2 * TH / H))

th = np.linspace(-TH, TH, OUT_W)
v = np.linspace(0, 1, OUT_H)
TT, VV = np.meshgrid(th, v)
Z = D - np.cos(TT)
X = CX + F * np.sin(TT) / Z
Y = TOP + F * VV * H / Z

def sample(X, Y):
    x0 = np.clip(np.floor(X).astype(int), 0, img.shape[1] - 2)
    y0 = np.clip(np.floor(Y).astype(int), 0, img.shape[0] - 2)
    fx = (X - x0)[..., None]; fy = (Y - y0)[..., None]
    a = img[y0, x0]; b = img[y0, x0 + 1]; c = img[y0 + 1, x0]; d = img[y0 + 1, x0 + 1]
    return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy

tex = sample(X, Y)
# white reference: blank band v in [0.03, 0.07]
ref = sample(X[0:1].repeat(40, 0), TOP + F * H * np.linspace(0.03, 0.07, 40)[:, None] / (D - np.cos(th))[None, :])
white = np.median(ref, axis=0)                     # (W,3)
white = np.maximum(white, 60)
target = np.array([247.0, 247.0, 245.0])
tex = tex * (target / white)[None, :, :]
tex = np.clip(tex, 0, 255).astype(np.uint8)
Image.fromarray(tex).save(out)
print(OUT_W, OUT_H, "arc_deg", 2 * math.degrees(TH), "height_radii", H)
