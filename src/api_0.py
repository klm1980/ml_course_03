import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from modules.api_data_models import CalcRequest, CalcResponse, Message

logging.basicConfig(
    format='[%(asctime)s][%(name)s][%(levelname)s] ~ %(message)s',
    level=logging.INFO,
    datefmt='%d-%b-%y %H:%M:%S'
)
logger = logging.getLogger()

DEFAULT_RESPONSES = {
    500: {'model': Message},    
}

app = FastAPI()

@app.get('/api/v1/health', response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info('Health check')

    return Message(message='Succsess.')

@app.get('/', responses={**DEFAULT_RESPONSES})
def he():
    logger.info('Hello')

    return {'Hello': ' world!!'}

@app.post('/api/v1/sum', response_model=CalcResponse, responses={**DEFAULT_RESPONSES})
def calc_sum(sum_request: CalcRequest):
    logger.info('Sum.')

    try:
        result = sum_request.a + sum_request.b
        return CalcResponse(result=result)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})

@app.post('/api/v1/sub', response_model=CalcResponse, responses={**DEFAULT_RESPONSES})
def calc_sub(sum_request: CalcRequest):
    logger.info('Sub.')

    try:
        result = sum_request.a - sum_request.b
        return CalcResponse(result=result)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})



