# Getting Started With Kafka
Apache Kafka ( Log as a Data Structure ?) 

Kafka is a collection of mutable append only logs
Primary component of storage is topic whcih represents data.


What is an event?
Thing which has just happened
User Interaction


It is notification ( element of whenness ) + state ( state is very small in size and represented as json or any object)

Event in Kafka is modelled as Key Value Pair

Keys and Values are sequences of bytes. Cuz Kafka internally is loosely types, externally its not

Key can be any complex object or any simple primitve types
Values are application domain object is the output for the event.


As part of the course, Created a Kafka Cluster, Added topics to that cluster. Added Events to that topic as key value pair. 
Each event got stored in the topic in different partitions. Using Confluent CLI, Produced and Consumed message to the topic.

What are topics ( little deep dive )
Topic is Kafka's fundamental unit of event organisation. 
You can consider it as a table in relational database.
Topics are log of events. 
They are append only. Logs can only be read by only seeking to a particular offset. Events are immutable in topic.
Topics are durable. 
Retention period is configurable.

Paritioning of topics:
1) Topics are stored in a partition ( basically topic data is distributed among paritions )
2) Which event goes to what topic? How is it decided? 
	a) Every event is represented a key value 
	b) If event doesnt have a key ( null ) then the data gets inserted into partitions into round robin fashion
	c) If event does have a key then it gets passed through a hash function and later it is modded with the total partitions you have.
	d) c point will ensure that all the events having same key goes to the same partition.


Brokers:
1) A Computer, Bare Metal Server , a container , virtual machine which runs a kafka process 
2) Each Broker Manages Partitions
3) Handle read and write requests
4) Manage replication of partitions
5) Intentionally very simple

Replication:
1) Replication is copies of partitions
2) Main Partitions is known as Leader partitions and replicated partitions are known as Follower Partitions
3) Read and write happens to leader partitions

Producers:
1) Producer is a client application
2) It puts message into Topic
3) It maintains connection pool with clusters.
4) Does network buffering 
5) Partitioning lives in the producer ( producer decides on which partition will the event go )
6) Retransmits messages upon failure

Consumers:
1) Client Application
2) Reads message on topics
3) Connection Pooling
4) Network Protocol
5) Horizontally and elastically scalable
6) Once you read a message , message still persist in the topic.
7) Ordering of message to be read by consumer is not guaranteed
7) When there are a lot of producers but just one consumer, that triggers an automatically rebalance process where the kafka cluster combined with consumer will attempt to distribute the traffic fairly across brokers.
8) When key is null , events / message are still guarantee order.

