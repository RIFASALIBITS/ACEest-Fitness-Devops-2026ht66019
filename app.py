from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

PROGRAMS = {
    "Fat Loss (FL)": {
        "workout": (
            "Mon: 5x5 Back Squat + AMRAP | "
            "Tue: EMOM 20min Assault Bike | "
            "Wed: Bench Press 21-15-9 | "
            "Thu: 10RFT Deadlifts/Box Jumps | "
            "Fri: 30min Active Recovery"
        ),
        "nutrition": (
            "B: 3 Egg Whites Oats Idli | "
            "L: Grilled Chicken Brown Rice | "
            "D: Fish Curry Millet Roti | "
            "Target: 2,000 kcal"
        ),
        "capacity": 15
    },
    "Muscle Gain (MG)": {
        "workout": (
            "Mon: Squat 5x5 | Tue: Bench 5x5 | "
            "Wed: Deadlift 4x6 | Thu: Front Squat 4x6 | "
            "Fri: Incline Press 4x10 | Sat: Barbell Rows 4x10"
        ),
        "nutrition": (
            "B: 4 Eggs PB Oats | "
            "L: Chicken Biryani (250g) | "
            "D: Mutton Curry Jeera Rice | "
            "Target: 3,200 kcal"
        ),
        "capacity": 15
    },
    "Beginner (BG)": {
        "workout": (
            "Circuit Training: Air Squats, Ring Rows, Push-ups | "
            "Focus: Technique Mastery & Form (90% Threshold)"
        ),
        "nutrition": (
            "Balanced Tamil Meals: Idli-Sambar, Rice-Dal, Chapati | "
            "Protein: 120g/day"
        ),
        "capacity": 20
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ACEest Fitness & Gym</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .card { background: white; padding: 20px; margin-bottom: 20px; }
        h1 { color: #333; }
        button { padding: 10px 15px; background: #007bff; color: white; }
    </style>
</head>
<body>
    <h1>ACEest FUNCTIONAL FITNESS</h1>
    <div class="card">
        <h3>Client Profile</h3>
        <form method="GET" action="/">
            <label>Select Program:</label>
            <select name="program">
                <option value="">Choose a fitness program</option>
                {% for key in programs.keys() %}
                    <option value="{{ key }}"
                      {% if selected_program == key %}selected{% endif %}>
                        {{ key }}
                    </option>
                {% endfor %}
            </select>
            <button type="submit">View Program</button>
        </form>
    </div>

    {% if details %}
    <div class="card">
        <h2>Weekly Workout Chart</h2>
        <p><strong>{{ selected_program }}</strong></p>
        <p>{{ details.workout }}</p>
        <h2>Daily Nutrition Plan</h2>
        <p>{{ details.nutrition }}</p>
    </div>
    {% else %}
    <div class="card">
        <p>Welcome to ACEest Fitness & Gym.</p>
    </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    selected_program = request.args.get("program")
    details = PROGRAMS.get(selected_program)
    return render_template_string(
        HTML_TEMPLATE,
        programs=PROGRAMS,
        selected_program=selected_program,
        details=details
    )


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/programs", methods=["GET"])
def list_programs():
    return jsonify({"programs": list(PROGRAMS.keys())}), 200


@app.route("/api/metrics", methods=["GET"])
def gym_metrics():
    total_capacity = sum(p["capacity"] for p in PROGRAMS.values())
    return jsonify({"total_capacity": total_capacity}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
