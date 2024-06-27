from flask import Flask, render_template, request, jsonify
import sum
# this is the flask fine
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form.get('topic')
        if topic:
            result = sum.summarize(topic)
            return render_template('index.html', summary=result['concise_report'], sources=result['sources'], topic=topic)
        else:
            return render_template('index.html', error="Please provide a topic.")
    return render_template('index.html')

#boom
if __name__ == '__main__':
    app.run(debug=True)
