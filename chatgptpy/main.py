from flask import Flask, request, render_template
import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_query():
    question = ""
    # process the question and generate an answer
    answer = "This is your answer"
    return render_template('index.html', answer=answer)


@app.route('/analysis')    
def analysis():         
    question = request.args.get('question')    
    print('question is working...>>'+question)

    if len(question) <= 0: 
        answer = "type your question"  
        return render_template('index.html', answer=answer) 
    else:
        answer = "question is not empty"



    url = "https://api.openai.com/v1/completions" 
    api_key = "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"     

    data = {
                    "model": "text-davinci-003",
                    "prompt" : question,
                    "max_tokens": 90                    
    }
        
    headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
    }                

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200: 
        response_data = response.json()
        answer = response_data["choices"][0]["text"].strip()
    else:
        answer = response.json()["error"]["message"]    

    return render_template('index.html', answer=answer, question=question)    




if __name__ == '__main__':
    app.run(debug=True)