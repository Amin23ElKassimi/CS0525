import http.client


ulr = input("Enter a URL (e.g., www.example.com): ")
port = input("Enter a port (default is 80): ")

if (not port):
    input_port = 80
else:
    input_port = int(port)

connection = http.client.HTTPConnection(ulr, input_port)
connection.request("OPTIONS", "/")
response = connection.getresponse()
print(f"Response status: {response.status}")

body_bytes = response.read()
body_sting = body_bytes.decode("utf-8")
print("Response body:")
print(body_sting)
connection.close()


