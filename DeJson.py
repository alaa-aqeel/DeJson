import json 


class DeJson:
	__dict__ = {}
	def __init__(self,Json: str =None,file: str =None):
		if not Json and not file:
			exit("DeJson(Json='String',file='pathFile')")

		Json_r = repr(Json).replace('"',"'")
		Json_r = str(Json_r)[1:-1].replace("'",'"')
		if file :
			Json_r =open(file,"r").read()
		try:
			self.__dict__ = json.loads(Json_r)
		except Exception as er:
			print(er);exit()

	def pprint(self):
		print(json.dumps(self.__dict__,sort_keys=True,indent=2))

	def __getattr__(self,key: str):
		return self.__dict__.get(key)
		
	def __getitem__(self,key: int):
		if type(self.__dict__) == dict:
			
			keys = self.__dict__.get(str(key))
			if keys and type(keys) == dict:
				return DeJson(Json=str(keys))
			else:
				return keys
		else:
			if type(self.__dict__[str(key)]) == dict:
				self.__dict__ = self.__dict__[key]
				return DeJson(Json=str(self.__dict__[key]))
			else:
				return self.__dict__[key]

# Json = "{'0':[1,2],'3':{'name':'alaa'}}"
Json = '{"works":[1,2,3,4],"0":[1,2],"3":{"name":"alaa"}}'
decode = DeJson(Json=Json) #  Json=string or file="test.json"
print(decode.works)   # key String  
print(decode[3].name) # key Integear = > inset name=alaa
print(decode[0])      # Key Integear 
