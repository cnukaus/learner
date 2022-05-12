## to consider
empty repo count  
missing feature - possiblity to derive?


## recently added
Number of commits  (query limited to original repo to fit API rate limit)
Relationship between commits to other gitcoin users' repo (in separate file)
Bio-fields authencity/effort(Number of profile fields populated)  
Twitter - # of mentions to other (gitcoin user)  
Twitter - # of times mentioned by other  
Twitter - likes, rt count

### evaluated
repo code complexity - possible, but needs to download repo file, so not useful because of API rate/bandwidth

## Feature hierarchy:  

[feature_source].[feature_set].[feature_name]

examples:  
"[gitcoin.co](http://gitcoin.co/)"."user_sybil"."sybil_likelihood"

"[api.github.com](http://api.github.com/)"."reputation"."followers"

"manual_googlesheets"."joe"."favouriteicons_count"


## Selection criteria:


1. Coverage: data fields  covering a significant amount of users are prefered

sparse features require more preparation effort to be useful, it is possible to include, maybe sometimes consider to derive/pca/merge sparse ones

2. Battle-tested: Used in previous GR rounds

3. Subject Matter Experts

4. Industry anti-spam resources (curated list, blacklist, IP addresses)

5. based on data source list (asked for it from dao members)

## V0.1.1 feature name and datatype

[api.github.com]
{"attribute":{"access":"public","API":"https://github.com/gitcoindao/SAD/blob/main/tests/data/extract_test.py"}}
- Number of repos, int
- Number of repos where fork=false, int
- Followers, int
- Followed, int
- watchers, int

   \#derived or row level
- total issues (summary from all repos), int
- highest open_issues_count of rep, int
- total forks (summary from all repos), int
- highest forks of rep, int
- total stars (summary from all repos), int
- highest stars of rep, int
- language, size, created_at, pushed_at date of each repo
-  Is the user followed by an authenticated github account - and history
- Most number of folders created across all repos, int
- Most number of files created across all reposts, int

[onchain][tokennomics.io]

{"attribute":{"access":"public","API":"http://tokenomics.io/gitcoin","contact":"tjayrush"},"source_code":"https://github.com/TrueBlocks/tokenomics.io"}}

data lineage (grant id to wallet address):
https://tokenomics.io/gitcoin/data/addresses.csv

endpoint here (https://gitcoin.co/api/v0.1/grants/?pk=<grant_id>)

- wallet address 


[gitcoin.co][behaviour]

{"attribute":{"access":"public","API":"https://gitcoin.co/grants/grants.json"}}


- Registration, Date/Time
- Last Activity, Date/Time
- kudos collected, int
- quest started, int
- Quest finished, int
- donation row level data (Address, grant, quantity, token, time)
- hackathon started count, int
- bounty started count, int
- bounty finished count,int
- hashed/salted IP Address row level/summary data (IP, date or first/last date range)
- browsing row level data (type of url, date)
- changed_default_preference, boolean
- count of activities in each GR round
  data source TBD

[gitcoin.co][attributes]



- Email domain (Inherit from Github), string
- Feedback row level/summary
- Built avatar, boolean
- Job status, string
- Location, string

{"attribute":{"access":"private", "data source":"MetaBase database"}}

 where the gitcoin/github IDs have wallet addresses stored for each.

Other potential:

- [gov.gitcoin.co]
- [snapshot.org]
- [withtally]
- [Discord activity raw data]



## rules

[user][self_defined_rules]  

Some data rules already on  [https://www.daostewards.xyz/](https://www.daostewards.xyz/))

## data lineage to provide

github_id <-> giticoin_id<-> grant_id <-> wallet_address mapping

## discussed anomality features:

https://gitcoin.co/artkkk user deleting their activity feed (so contribution shows $0 funded?)  

Repeat Worker score


## Ref

[GR10 antifraud report blockscience] (https://medium.com/block-science/evaluating-the-anti-fraud-results-for-gitcoin-round-10-cec9277ce5b2)
combined dialog with Omnianalytics, Disruption

[internal Notion page of Anti-sybil workstream](https://www.notion.so/gitcoin/06fad27dbd2d49468aa810c92f1f28c2?v=0e00edb4b94b4555a3d7b71b8d193d6c)
