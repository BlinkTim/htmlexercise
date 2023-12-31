from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()




templates = Jinja2Templates(directory="./")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    name = "Tim Niggemann"
    skill1 = "HTML"
    skill2 = "Python"
    return templates.TemplateResponse("index.html", {"request": request, "name": name,"skill1": skill1, "skill2": skill2  })

@app.get("/contact", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request}) 

@app.post("/contact", response_class=HTMLResponse)
async def submit(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8080)
