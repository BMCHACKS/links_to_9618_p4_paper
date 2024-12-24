import os
from flask import Flask, request, jsonify
import urllib.request
from flask_cors import CORS

app = Flask(__name__)

# Allow only the frontend domain (GitHub Pages) to access your backend
CORS(app, resources={r"/*": {"origins": "https://bmchacks.github.io"}})

@app.route('/links', methods=['POST'])
def get_links():
    data = request.get_json()
    year = data['year']
    main_text_link = "https://pastpapers.co/cie/A-Level/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/"
    links = []
    summer = True
    for sw in range(2):
        for y in range(1, 5):
            for variant in range(1, 4):
                if summer: 
                    links.append(f"{main_text_link}202{y}-May-June/9618_s2{y}_qp_4{variant}.pdf")
                else:
                    links.append(f"{main_text_link}202{y}-Oct-Nov/9618_w2{y}_qp_4{variant}.pdf")
        summer = False

    valid_links = []
    for link in links:
        if year == link[len(main_text_link): len(main_text_link)+4]: 
            try:
                response = urllib.request.urlopen(link).getcode()
                if response == 200:
                    valid_links.append(link)
            except:
                pass
    return jsonify({"links": valid_links})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
