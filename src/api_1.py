import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from modules.api_data_models import HouseInfo, HousePrice, Message
from modules.simple_ml_models import HousePriceModel

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
app.model = HousePriceModel()

@app.get('/api/v1/health', response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info('Health check')

    return Message(message='Succsess.')


@app.post('/api/v1/predict', response_model=HousePrice, responses={**DEFAULT_RESPONSES})
def predict(house_info: HouseInfo):
    logger.info('Predict')

    try:
        price = app.model(
            n_floors = house_info.n_floors,
            area = house_info.area,
            heating = house_info.heating,
        )
        return HousePrice(price=price)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})
