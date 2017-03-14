printf "\n[LAST CLOSED LEDGER]\n"; sleep 1
curl -X POST -d '{ "method": "ledger_closed", "params": [ {} ] }' http://s1.ripple.com:51234 2>/dev/null | python -m json.tool

printf "\n[LEDGER DATA]\n"; sleep 1
curl -X POST -d '{ "method": "ledger_data", "params": [ { "binary": false, "ledger_hash": "32549143F20C2417406ED614EF8A98D19AE525E947E0394E1542C5C8C255571E", "limit": 5 } ] }' http://s1.ripple.com:51234 2>/dev/null | python -m json.tool

printf "\n[TRANSACTION DETAIL]\n"; sleep 1
curl -X POST -d '{ "method": "tx", "params": [ { "transaction": "E24ACA2991C4DAA79B198EE9ADF9F8CB0E47561BA9B99CBA3B330E1AEB8D76A8", "binary": false } ] }' http://s1.ripple.com:51234 2>/dev/null | python -m json.tool

printf "\n[ACCOUNT INFO]\n"; sleep 1
curl -X POST -d '{ "method" : "account_info", "params" : [ { "account" : "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"} ] }' http://s1.ripple.com:51234 2>/dev/null | python -m json.tool
