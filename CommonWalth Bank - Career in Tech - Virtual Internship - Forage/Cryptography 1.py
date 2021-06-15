from base64 import b64decode as b64d
from base64 import b64encode as b64e
from random import randint



if __name__ == '__main__':
	flag = "Vm0xd1MwNUdXWGxWV0dSUFZsZG9XRmx0ZUV0V01XeDBaVWRHVjFac1NsWlZWbEpIVlRKS1NHVkdXbFpOVmtwWVZrZDRTMk14V25GWApiSEJYVWxSV2VWZFdaRFJaVjAxNFZHNUdWQXBpUmxwWVdXdG9RMUpXV2toTlZGSmFWbTFTV0ZkcmFFOVZkM0JwVjBkb2RsWkdXbUZqCk1EQjRWMjVLWVZKRlNsQlZha0poVFVaYVNFNVZkRlZhTTBKWVdXdFdkMVZXV2xkaFNHUnFDazFXV25wV01uUmhWakpLY21ORk9WZGkKV0dob1ZXcEdkMVpzV25SU2JGcFNWMFZLVmxaWE1UQmpiVlpYV2taV1ZXSnRVbkZEYXpGWFVtcFNWMDFxVmxSV1ZFcEhZMnMxVjFWcwpjRmNLVWxWd2IxWldVa2RXYlZaSFYyNVNVMkpGTlZkV01GWkxaR3hrVjFWclpGZGhlbFpZVld4b2MxZHRWblJsUmtwRVlrWmFXVlF3ClVuTlNSbkEyVFVSc1JGcDZNRGxEWnowOUNnPT0K"

	print ("Try to get the flag reversing the python script that generated it!")

	for i in range (10):
		try:
			flag=b64d(flag)
		except:
			print("Done")
			break
		flag=flag.strip()
		print ("Decypted",i,"times :",flag)
	
	
	