import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class SNS:
    def __init__(self):
        self.topics = {}

    def create_topic(self, name):
        if name in self.topics:
            raise Exception("Topic already exists")
        self.topics[name] = []
        logging.info(f"Created topic: {name}")
        return name

    def subscribe(self, topic, endpoint):
        if topic not in self.topics:
            raise Exception("Topic does not exist")
        self.topics[topic].append(endpoint)
        logging.info(f"Subscribed {endpoint.name} to topic: {topic}")

    def publish(self, topic, message):
        if topic not in self.topics:
            raise Exception("Topic does not exist")
        for endpoint in self.topics[topic]:
            endpoint.notify(message)
            logging.info(f"Published message to {endpoint.name}: {message}")

class Endpoint:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"Notification to {self.name}: {message}")

# Example usage
try:
    sns = SNS()
    email = Endpoint("Email")
    sms = Endpoint("SMS")
    topic = sns.create_topic("MyTopic")
    sns.subscribe(topic, email)
    sns.subscribe(topic, sms)
    sns.publish(topic, "Hello, world")
except Exception as e:
    logging.error(f"Error: {e}")
