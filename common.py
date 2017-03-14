
import json, logging, requests
from pymongo import MongoClient


# configure logging
verbosity = logging.INFO
logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(format='%(asctime)-15s %(levelname)s %(message)s', level=verbosity)
logger = logging.getLogger(__name__)


# db
client = MongoClient()
db = client['ripple']


# make RPC request
def fetch(request):
	base_url = 'http://s1.ripple.com:51234'
	payload = json.dumps(request)
	logger.debug('REQUEST {}'.format(payload))
	response = requests.post(base_url, data=payload)
	logger.debug('RESPONSE [{}] {}'.format(response.status_code, response.reason))
	return json.loads(response.text)['result']


def pluralize(qty):
    return '' if qty == 1 else 's'
