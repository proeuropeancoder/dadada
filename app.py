from flask import Flask, render_template_string, request
from match_engine import MatchSimulator

app = Flask(__name__)
simulator = MatchSimulator()

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Football Match Simulator</title>
    <style>
        body { font-family: Arial; background: #f0f0f0; padding: 20px; }
        h1 { color: #333; }
        .section { margin-bottom: 30px; }
        .commentary { background: #fff; padding: 10px; border-radius: 5px; max-height: 300px; overflow-y: scroll; }
        .score { font-size: 24px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>⚽ Football Match Simulator</h1>

    <div class="section">
        <h2>Starting XI (3-4-3)</h2>
        <ul>
            <li>GK: {{ xi['GK'] }}</li>
            <li>CBs: {{ xi['CB']|join(', ') }}</li>
            <li>LWB: {{ xi['LWB'] }}</li>
            <li>RWB: {{ xi['RWB'] }}</li>
            <li>CMs: {{ xi['CM']|join(', ') }}</li>
            <li>LW: {{ xi['LW'] }}</li>
            <li>ST: {{ xi['ST'] }}</li>
            <li>RW: {{ xi['RW'] }}</li>
        </ul>
    </div>

    <div class="section">
        <h2>Bench</h2>
        <p>{{ bench|join(', ') }}</p>
    </div>

    <div class="section">
        <form method="POST" action="/simulate">
            <button type="submit">Start Match Simulation</button>
        </form>
    </div>

    {% if commentary %}
    <div class="section">
        <h2>Match Commentary</h2>
        <div class="score">Score: {{ score[0] }} - {{ score[1] }}</div>
        <div class="commentary">
            {% for line in commentary %}
                <p>{{ line }}</p>
            {% endfor %}
        </div>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(template, xi=simulator.starting_xi, bench=simulator.bench, commentary=None, score=simulator.score)

@app.route('/simulate', methods=['POST'])
def simulate():
    commentary, score = simulator.run_match()
    return render_template_string(template, xi=simulator.starting_xi, bench=simulator.bench, commentary=commentary, score=score)

if __name__ == '__main__':
    app.run(debug=True)

