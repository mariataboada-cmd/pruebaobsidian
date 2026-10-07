---
workflow: general-video
flow: automation
storyboard: no
message: "El bote de Minimelis Biotina se abre y sus gominolas flotan: producto premium y apetecible"
destination: social (Reels / TikTok / Stories)
aspect: 9:16 (1080x1920)
language: es
length: 12.4s (intro 4.4s + loop seamless de 8s)
---

## Intent

Anuncio 3D del bote real de Minimelis Biotina (foto de referencia del usuario).
"Quiero que sea un vídeo del bote abriéndose la tapa y saliendo tres gominolas
flotando y que se queden entre la tapa y el bote y se queden ahí como flotando
seguido en loop."

## Must-haves (del brief original)

- Fidelidad absoluta al envase: etiqueta, logotipo, colores, tipografía y proporciones de la foto.
- No inventar ni modificar branding ni texto.
- Look de publicidad premium: iluminación de estudio, key suave, rim light, sombras suaves, sin estética cartoon.
- Movimientos de cámara lentos y suaves.

## Decisions (inferred, not answered by the user)

- 3D en tiempo real con Three.js (PBR, transmisión, entorno HDR), no ray tracing.
- Etiqueta: desenrollada de la foto con un modelo de cámara ajustado a la curvatura (assets/label-front.png, tools/unwrap_label.py). Cubre 160° frontales; el bote solo se balancea ±4°, así que nunca se ve la parte no fotografiada.
- Gominolas con forma de osito, como las que se ven dentro del bote en la foto.
- Formato vertical 1080x1920; fondo frambuesa oscuro tomado del color de la foto.

## Assets

- assets/src/reference.jpg — foto original del usuario.
