import pickle
from fastapi import FastAPI
from pydantic import BaseModel


class Saida(BaseModel):
    survived: bool
    status: int = 200
    message: str = "A predição foi concluida!"

app = FastAPI()

@app.post("/model", response_model = Saida)

def titanic(sex: int, age: float, lifeboat: int, p_class: int):
    
    """
    Prediz a possibilidade de sobrevivencia ao naufrágio do Titanic, levando em consideração:
    - ***sex***: sexo ---> masculino (0) e feminino (1) ;
    - ***age***: idade ---> fracionário, exemplo: 10.6 ;
    - ***lifeboat***: número do barco salva vidas ---> 0;
    - ***p_class***: classe no navio ---> primeira classe (1)  e econômica (3).
    """
    

    with open("model/Titanic.pkl", "rb") as fid: 
        titanic = pickle.load(fid)
        predicao = titanic([sex, age, lifeboat, p_class])
    
    return {
            {"survived": bool(predicao)},	
            {"status": 200},
	        {"message": "A predição foi concluida!"}
            }
        

@app.get("/")
def get():
    return {"API de predição de sobrevivência ao naufrágio do Titanic"}


@app.get("/model")
def saida():
    return (
                {"survived": bool(titanic)},	
                {"status": 200},
	            {"message": "A predição foi concluida!"}
            )