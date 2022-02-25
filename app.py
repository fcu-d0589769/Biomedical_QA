from fastapi import Body, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, constr
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline,AutoModelForQuestionAnswering


class DemoRequest(BaseModel):
    question: constr(max_length=512)
    keyword: str
class NERRequest(BaseModel):
    sentance: constr(max_length=512)
class QARequest(BaseModel):
    maintext: constr(max_length=512)
    subtext: constr(max_length=512)

class NERItem(BaseModel):
    entity: str
    score: float
    index: int
    word: str
    start: int
    end: int


app = FastAPI(
    title="biomedicine",
    description="A NLP Demo Website.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ner_tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
ner_model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
ner_pipeline = pipeline("ner", model=ner_model, tokenizer=ner_tokenizer)

#text-generate(QA,QG,Summarization .etc)
generation_tokenizer=AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
generation_model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
generation_pipeline=pipeline("question-answering", model=generation_model, tokenizer=generation_tokenizer)


###
import csv
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from collections import Counter
with open('biomedicine.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)

    for r in rows:
        pubmed = r




model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)


def biomedicine_QA(question, keyword):

    # max 5 keyword
    #keyword = ['HIV','therapy']
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
        QA_input={'question': question, 'context':c}
        # QA_input={'question': 'what is the risk of using antiretroviral?', 'context':c}
        answers.append(nlp(QA_input)["answer"])
        print(nlp(QA_input)["answer"])

    n = 3
    result = Counter(answers).most_common(n)
    print(result)
    top_n = []
    for r in result:
        top_n.append(r[0])

    return top_n
    ###





@app.get("/")
async def root():
    return RedirectResponse("docs")


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    return templates.TemplateResponse(f"{page_name}.html", {"request": request})


#
# NER
#


@app.post("/ner")
async def ner(
    ner_request: NERRequest = Body(
        None,
        examples={
            "Example 1": {
                "value": {"sentance": "My name is Wolfgang and I live in Berlin"}
            },
            "Example 2": {
                "value": {"sentance": "My name is Sarah and I live in London"}
            },
            "Example 3": {
                "value": {
                    "sentance": "My name is Clara and I live in Berkeley, California."
                }
            },
        },
    )
):
    results = ner_pipeline(ner_request.sentance)
    validated = [NERItem(**item) for item in results]
    return validated

@app.post("/qa")
async def qa(
    qa_request: QARequest = Body(
        None,
        
    )
):
    print(qa_request)
    model_input={
        "question":qa_request.maintext,
        "context":qa_request.subtext
    }
    results = generation_pipeline(model_input)
    # validated = [NERItem(**item) for item in results]
    return results


@app.post("/demo")
async def demo(
    demo_request: DemoRequest = Body(
        None,
        
    )
):
    keyword = demo_request.keyword.split(',')
    print(demo_request)
    model_input={
        "question":demo_request.question,
        "keyword":demo_request.keyword
    }
    results = biomedicine_QA(demo_request.question,keyword)
    print(results)
    return results