# app.py
from flask import Flask, request, render_template_string
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        year = request.form.get('year')
        
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

        for link in links:
            if year == link[len(main_text_link): len(main_text_link)+4]: 
                try:
                    response = urllib.request.urlopen(link).getcode()
                    if response == 200:            
                        output += f"<div>{link}</div>"
                except:
                    pass

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Console</title>
    <style>
        body { 
            font-family: monospace; 
            background-color: black; 
            color: green; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            margin: 0; 
        }
        .console { 
            background-color: black; 
            padding: 20px; 
            border-radius: 10px; 
            width: 80%; 
            max-width: 800px; 
            box-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
        }
        .console input { 
            background-color: #333; 
            color: green; 
            border: 1px solid green; 
            padding: 5px; 
            width: calc(100% - 12px); 
            margin-bottom: 10px; 
        }
        .console button { 
            background-color: green; 
            color: black; 
            border: none; 
            padding: 10px 20px; 
            cursor: pointer; 
            width: 100%;
        }
        .console button:hover {
            background-color: #00ff00;
        }
        .output { 
            max-height: 400px; 
            overflow-y: auto; 
            margin-top: 10px; 
            padding: 10px; 
            background-color: #222; 
            border-radius: 5px;
        }
        .output div {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="console">
        <form method="POST">
            <label for="year">Enter the year:</label>
            <input type="text" name="year" id="year" required>
            <button type="submit">Run</button>
        </form>
        <div class="output">
            {{output|safe}}
        </div>
    </div>
</body>
</html>
    ''', output=output)

if __name__ == '__main__':
    app.run(debug=True)
