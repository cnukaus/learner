tjayrush — 01/10/2022
@Richard_ 

There's an API here: https://gitcoin.co/grants/grants.json, but it's not really helpful because it doesn't connect the grant_id to the address.

There's also and endpoint here (https://gitcoin.co/api/v0.1/grants/?pk=<grant_id>), but that also is not that easy to use.

(If anyone responsible for the GitCoin API is listening, to make it much more easy to use, include grant_id in the first response.)

What we did was create a shell script that sequentially runs through the grant_ids between 0 and 5000 to download the full definition of the grant by grant_id.

We then extracted this file: https://tokenomics.io/gitcoin/data/addresses.csv. It's not perfect data, so it needs to be cleaned a bit, but it gives you the map you're asking for

https://docs.gitcoin.co/mk_rest_api/

[https://docs.gitcoin.co/mk_rest_api/](https://docs.gitcoin.co/mk_rest_api/)
There's also and endpoint here ([https://gitcoin.co/api/v0.1/grants/?pk=](https://gitcoin.co/api/v0.1/grants/?pk=)<grant_id>), but that also is not that easy to use.

(If anyone responsible for the GitCoin API is listening, to make it much more easy to use, include `grant_id` in the first response.)

What we did was create a shell script that sequentially runs through the grant_ids between 0 and 5000 to download the full definition of the grant by `grant_id`.

We then extracted this file: [https://tokenomics.io/gitcoin/data/addresses.csv](https://tokenomics.io/gitcoin/data/addresses.csv). It's not perfect data, so it needs to be cleaned a bit, but it gives you the map you're asking for （grant_id, wallet address)