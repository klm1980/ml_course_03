import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from modules.api_data_models import TextInput, TextOutput, Message
from modules.simple_ml_models import SantimentModel

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
app.model = SantimentModel()

@app.get('/api/v1/health', response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info('Health check')

    return Message(message='Succsess.')


@app.post('/api/v1/predict', response_model=TextOutput, responses={**DEFAULT_RESPONSES})
def predict(text_input: TextInput):
    logger.info('Predict')

    try:
        res = app.model(
            text = text_input.text            
        )
        return TextOutput(**res)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})
