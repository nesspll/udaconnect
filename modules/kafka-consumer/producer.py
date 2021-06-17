from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
msg1=dict({'first_name':'John','last_name':'Doe','company_name':'PlaySmar Inc.'})
#msg2=dict({'id':64,'person_id':27 , 'creation_time':'2020-01-05 10:37:06.000000', 'latitude' : '-122.290883','longitude':'37.55363'})
producer.send('test', bytes(str(msg1), 'utf-8'))
#producer.send('test', bytes(str(msg2), 'utf-8'))
producer.flush()

{'person_id':8, 'creation_time':'2020-01-05 10:37:06.000000', 'latitude' : '-122.290883','longitude':'37.55363'}