from flask import Flask
from flask import request
import dataProcessing
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route("/notify")
def notify():
    # thực hiện tính toán lại model
    data = request.data
    # df_add = pd.DataFrame(data)
    return data


@app.route('/getOrther',methods = ['POST'])
def getOrther():
    if request.method == 'POST':
        info = request.data
        # dùng data tính độ phù hợp
        return ''

if __name__ == '__main__':
    app.run()

# {
#   "testCode": "string123",
#   "testName": "Thi thử",
#   "sections": [
#     {
#       "sectionName": "Phần 1",
#       "questionSections": [
#         {
#           "questionId": "eff8b8f1-fcf4-4a0e-9c1f-08da39b35710"
#         }
#       ]
#     }
#   ]
# }