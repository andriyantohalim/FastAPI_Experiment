from fastapi import FastAPI, APIRouter

app = FastAPI(title="Hello App")


# router_main = APIRouter()
# @router_main.get("/")
# def main():
#     return { "hello world": "Hello"}


@app.get("/")
async def read_main():
    return {"message": "hello world from main app"}


# subapi = FastAPI()


# @subapi.get("/")
# def read_slash():
#     return {"message": "Hello world from slash"}


# @subapi.get("/sub")
# def read_sub():
#     return {"message": "Hello world from sub API"}


router_test_1 = APIRouter()

@router_test_1.get("/")
def test_1():
    return {"msg":"test"}

@router_test_1.post("/")
def test_2():
    return {"msg":"test"}

@router_test_1.get("/testtest")
def test_3():
    return {"msg":"test"}

@router_test_1.post("/testtest")
def test_4():
    return {"msg":"test"}


router_test_2 = APIRouter()

@router_test_2.get("/")
def test_1():
    return {"msg":"test"}

@router_test_2.post("/")
def test_2():
    return {"msg":"test"}

@router_test_2.get("/testtest")
def test_3():
    return {"msg":"test"}

@router_test_2.post("/testtest")
def test_4():
    '''
    Name: test
    Description: test test
    :return: None
    '''
    return {"msg":"test"}


# app.mount("/", subapi)
# app.mount("/subapi", subapi)
# app.include_router(router_main, tags=["testmain"])
app.include_router(router_test_1, prefix="/test1", tags=["testroute1"])
app.include_router(router_test_2, prefix="/test2", tags=["testroute2"])