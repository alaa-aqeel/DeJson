# DeJson


## Using ##
```

>>> # Json = "{'0':[1,2],'3':{'name':'alaa'}}"
>>> Json = '{"works":[1,2,3,4],"0":[1,2],"3":{"name":"alaa"}}'
>>> decode = DeJson(Json=Json) #  Json=string or file="test.json"
>>> print(decode.works)   # key String  
>>> print(decode[3].name) # key Integear = > inset name=alaa
>>> print(decode[0])      # Key Integear 
>>> decode.pprint()  #// print all 

```

## Result ##
```
>> [1, 2, 3, 4]
>> alaa
>> [1, 2]
>> {
  "0": [
      1,
      2
    ],
  "3": {
      "name": "alaa"
    },
  "works": [
      1,
      2,
      3,
      4
    ]
}

```
