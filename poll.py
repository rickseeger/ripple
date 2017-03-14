#!/usr/bin/env python


import time
from common import fetch, pluralize, logger, db


period_sleep = 1


# polling loop
while (True):
	time.sleep(period_sleep)

	# fetch last known ledger index
	last_seq = int(db.ledgers.find_one(sort=[('seq', -1)])['seq'])
  
	# get latest closed ledger
	response = fetch({ "method": "ledger_closed", "params": [ {} ] })
	seq = response['ledger_index']
	logger.info('FETCHED ledger {}'.format(seq))

	# how many did we miss?
	delta = seq - last_seq
	if (delta == 0):
		logger.info('local database is up to date')
		continue
	else:
		logger.info('LAGGING by {} ledger{}'.format(delta, pluralize(delta)))

    # parse missing ledgers
	for idx in range(last_seq+1, seq+1):

		# ledgerEntryType
		#  AccountRoot - describes single account object with balance
		#  DirectoryNode - links to other nodes
		#  Offer - offer to exchange currencies
		#  PaymentChannel - an off chain payment channel ref with Amount and Balance
		#  RippleState - connects two accounts in single currency
		#  SignerList - list of signers for multi-sign
		
		# get ledger detail
		ledger = fetch({ "method": "ledger_data",
						 "params": [{ "binary": False,
                                      "ledger_index": idx
						 }]
		});

		hash = ledger['ledger_hash']
		db.ledgers.insert({ 'seq': idx, 'hash': hash })
		logger.info('UPDATED ledger {} of {} IDX {} HASH {}'.format(idx-last_seq, seq-last_seq, idx, hash[:8]))

		n = 0
		for entry in ledger['state']:
			if entry['LedgerEntryType'] == 'AccountRoot' and \
			   'Balance' in entry.keys() and \
			   'Account' in entry.keys():

				acct = entry['Account']
				bal = entry['Balance']

				# update mongo balances table
          
				logger.debug('n:{}; acct: {}  balance: {}'.format(n, acct, bal))
				n += 1
  
		logger.info('UPDATED {} AccountRoot record{}'.format(n, pluralize(n)))
