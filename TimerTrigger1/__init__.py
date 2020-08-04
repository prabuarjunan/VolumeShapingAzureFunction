import datetime
import logging
from . import volumeShapingsizing_dealloc
import azure.functions as func

def main(mytimer1: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    volumeShapingsizing.update_volume()
    if mytimer1.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)