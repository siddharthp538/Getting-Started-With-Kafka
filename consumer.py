#!/usr/bin/env python

from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Consumer

if __name__ == "__main__":
        parser = ArgumentParser()
        parser.add_argument('config_file' , type= FileType('r'))
        args = parser.parse_args()

        config_parser = ConfigParser()
        config_parser.read_file(args.config_file)
        config = dict(config_parser['default'])
        config.update(config_parser['consumer'])

        consumer = Consumer(config)

        topic = "poems"
        consumer.subscribe([topic])

        try:
                while True:
                        msg = consumer.poll(1.0)
                        if msg is None:
                                print("Wating...")
                        elif msg.error():
                                print("Error...")
                        else:
                                print("Consumed Event From Topic {topic} : key {key:12} , value = {value:12}".format(topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
        except KeyBoardInterrupt:
                pass
        finally:
                consumer.close()


