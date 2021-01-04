# vcokltfre/max-lb

## An incredibly simple load balancer for IBM's MAX toxic comment classifier

#### PRs won't be accepted. This is simply a way of having the code available for use elsewhere by me, and you if you find it useful as is.

`POST http://addr:7777/` \
data:
```json
{
  "text":"your text"
}
```
response:
```json
{
  "toxic": 0.9567647576332092,
  "severe_toxic": 0.08615504205226898,
  "obscene": 0.9610628485679626,
  "threat": 0.007074730470776558,
  "insult": 0.030704936012625694,
  "identity_hate": 0.002753487089648843
}
```