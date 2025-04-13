from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyCpETP7d4rQccLrmmrdIJwyt8J0w9TEYeM"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_hypothesis', methods=['POST'])
def generate_hypothesis():
    try:
        data = request.json
        topic = data.get('topic', '').strip()
        
        if not topic:
            return jsonify({'error': 'Please provide a topic'}), 400

        prompt = f"""Generate a detailed hypothesis for the following topic: {topic}
        Format the response in the following structure:

        1. Main Hypothesis Statement
        ● [Provide the main hypothesis]

        2. Supporting Sub-hypotheses
        ● [First sub-hypothesis]
        ● [Second sub-hypothesis]
        ● [Third sub-hypothesis]

        3. Key Variables
        ● [First variable]
        ● [Second variable]
        ● [Third variable]

        4. Research Methods
        ● [First method]
        ● [Second method]
        ● [Third method]

        5. Expected Outcomes
        ● [First expected outcome]
        ● [Second expected outcome]
        ● [Third expected outcome]

        6. Limitations
        ● [First limitation]
        ● [Second limitation]
        ● [Third limitation]

        Important Formatting Instructions:
        - Use black circle bullet points (●) for all sub-points
        - Do not use any stars (*) in the titles
        - Keep each section clearly separated
        - Make the response clear and structured
        - Use simple language suitable for students
        - Ensure all section titles are properly numbered and formatted"""

        response = model.generate_content(prompt)
        return jsonify({'hypothesis': response.text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
