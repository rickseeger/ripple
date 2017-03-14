# account info
#curl -X POST -d '{ "method" : "account_info", "params" : [ { "account" : "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"} ] }' http://s1.ripple.com:51234

# last closed ledger
#curl -X POST -d '{ "method": "ledger_closed", "params": [ {} ] }' http://s1.ripple.com:51234

# transaction detail
#curl -X POST -d '{ "method": "tx", "params": [ { "transaction": "E08D6E9754025BA2534A78707605E0601F03ACE063687A0CA1BDDACFCD1698C7", "binary": false } ] }' http://s1.ripple.com:51234

# ledger entry
#curl -X POST -d '{ "id": 1, "method": "ledger_entry", "type": "account_root", "account_root": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59", "ledger_index": "validated"  }' http://s1.ripple.com:51234

# get balance
#curl -X POST -d '{ "id": 2, "method": "account_info", "account": "r9cZA1mLK5R5Am25ArfXFmqgNwjZgnfk59" }' http://s1.ripple.com:51234

