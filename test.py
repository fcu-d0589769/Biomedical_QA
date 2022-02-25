# import os, sys
# os.environ['SPARK_HOME'] = "/user_data/spark"
# os.environ['PYSPARK_PYTHON'] = "/user_data/spark/python"
# sys.path.append("/user_data/spark/python")
# sys.path.append("/user_data/spark/python/lib/pyspark.zip")
# sys.path.append("/user_data/spark/python/lib/py4j-0.10.9-src.zip")
import csv
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from collections import Counter
with open('biomedicine.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)

    for r in rows:
        pubmed = r




model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'what is the better therapy for HIV?',
    'context': 'In patients with advanced HIV disease , zidovudine appears to be more effective than didanosine as initial therapy ; however , some patients with advanced HIV disease may benefit from a change to didanosine therapy after as little as 8 to 16 weeks of therapy with zidovudine '
}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# max 5 keyword
keyword = ['HIV','therapy']
context = []
flag = 0
for p in pubmed:
    for k in keyword:
        if k in p:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        context.append(p)

answers = []
for c in context:
    if c == '':
        continue
    QA_input={'question': 'what is the therapy for the HIV?', 'context':c}
    # QA_input={'question': 'what is the risk of using antiretroviral?', 'context':c}
    answers.append(nlp(QA_input)["answer"])
    print(nlp(QA_input)["answer"])

result = Counter(answers).most_common(3)
print(result[0])
