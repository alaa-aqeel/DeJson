# DeJson


##Using##
```

# Json = "{'0':[1,2],'3':{'name':'alaa'}}"
Json = '{"works":[1,2,3,4],"0":[1,2],"3":{"name":"alaa"}}'
decode = DeJson(Json=Json) #  Json=string or file="test.json"
print(decode.works)   # key String  
print(decode[3].name) # key Integear = > inset name=alaa
print(decode[0])      # Key Integear 

```
