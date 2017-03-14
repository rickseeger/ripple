#!/usr/bin/env python


# artificially set last known ledger index to a recent value


import sys
from common import db, fetch, logger, pluralize


# required parameter: how many ledgers behind we should be
delta = None
try:
    delta = int(sys.argv[1])
except:
    sys.stderr.write('usage: {} delta\n'.format(sys.argv[0]))
    exit(1)


# wipe ledger collection
db.ledgers.remove();
logger.info('TRUNCATED ledgers collection');


# get latest closed ledger
response = fetch({ "method": "ledger_closed", "params": [ {} ] })
idx = response['ledger_index']
hash = response['ledger_hash']
logger.info('RETRIEVED closed ledger IDX {} HASH {}'.format(idx, hash[:8]))


# go back
logger.info('REWINDING {} ledger{}'.format(delta, pluralize(delta)))
idx -= delta
response = fetch({ "method": "ledger_data",
				   "params": [{ "binary": False,
								"ledger_index": idx
				   }]
});


# make entry in ledgers collection
idx = response['ledger_index']
hash = response['ledger_hash']
logger.info('INITIALIZED ledgers collection IDX {} HASH {}'.format(idx, hash[:8]));
db.ledgers.insert({ 'seq': idx, 'hash': hash })
