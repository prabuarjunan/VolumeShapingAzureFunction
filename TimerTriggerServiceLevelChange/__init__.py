import datetime
import logging
from . import volumeShapingsizing_serviceLevel 
import azure.functions as func

def main(mytimer2: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    volumeShapingsizing_serviceLevel.update_CapacityPool()
    if mytimer2.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)