import grpc
import services_pb2
import services_pb2_grpc
from services_pb2 import PersonMessage, LocationMessage

from datetime import datetime

# open a gRPC channel
channel = grpc.insecure_channel('localhost:30033')

# create a stub (client)
stub = services_pb2_grpc.CallServiceStub(channel)

# create a valid request message
person = PersonMessage(id=29, first_name="Ness" , last_name="Pllana", company_name="cuburn")
#location = LocationMessage(person_id=5,creation_time="2020-01-05T10:37:06",latitude="20.518730",longitude="22.992470")
#stub.create_location(location)
stub.create_person(person)
print(person)
#print(location)

# make the call
#stub.create_person(person)