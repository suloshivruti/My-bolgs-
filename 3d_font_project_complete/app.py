from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-font', methods=['POST'])
def generate_3d_font():
    data = request.json
    text = data.get("text", "3D Font")
    font_size = int(data.get("size", 100))
    color = data.get("color", "#ff6347")
    
    img = Image.new('RGBA', (800, 400), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)
    
    shadow_color = "#333333"
    for offset in range(10):
        draw.text((50 + offset, 100 + offset), text, font=font, fill=shadow_color)
    draw.text((50, 100), text, font=font, fill=color)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
