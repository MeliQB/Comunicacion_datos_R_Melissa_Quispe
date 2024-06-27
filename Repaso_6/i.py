import logging

# Configura el registro de logs con nivel "INFO" y un formato específico
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

class SNS:
    """
    Clase que simula el funcionamiento de Amazon Simple Notification Service (SNS).
    """
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar los temas
        self.topics = {}

    def create_topic(self, name):
        """
        Crea un nuevo tema con el nombre especificado.
        
        Args:
            name (str): El nombre del tema a crear.
        
        Raises:
            Exception: Si el tema ya existe.
        
        Returns:
            str: El nombre del tema creado.
        """
        # Verifica si el nombre del tema ya existe
        if name in self.topics:
            raise Exception("Topic already exists")
        
        # Agrega el nuevo tema al diccionario de temas
        self.topics[name] = []
        
        # Registra un mensaje informativo sobre la creación del tema
        logging.info(f"Created topic: {name}")
        
        return name

    def subscribe(self, topic, endpoint):
        """
        Suscribe un endpoint a un tema existente.
        
        Args:
            topic (str): El nombre del tema al que suscribir el endpoint.
            endpoint (Endpoint): El endpoint a suscribir.
        
        Raises:
            Exception: Si el tema no existe.
        """
        # Verifica si el tema existe
        if topic not in self.topics:
            raise Exception("Topic does not exist")
        
        # Agrega el endpoint a la lista de suscriptores del tema
        self.topics[topic].append(endpoint)
        
        # Registra un mensaje informativo sobre la suscripción del endpoint
        logging.info(f"Subscribed {endpoint.name} to topic: {topic}")

    def publish(self, topic, message):
        """
        Publica un mensaje en un tema existente.
        
        Args:
            topic (str): El nombre del tema en el que publicar el mensaje.
            message (str): El mensaje a publicar.
        
        Raises:
            Exception: Si el tema no existe.
        """
        # Verifica si el tema existe
        if topic not in self.topics:
            raise Exception("Topic does not exist")
        
        # Envía el mensaje a cada endpoint suscrito al tema
        for endpoint in self.topics[topic]:
            endpoint.notify(message)
            
            # Registra un mensaje informativo sobre la publicación del mensaje
            logging.info(f"Published message to {endpoint.name}: {message}")

class Endpoint:
    """
    Clase que representa un endpoint que puede recibir notificaciones.
    """
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        """
        Recibe y muestra una notificación.
        
        Args:
            message (str): El mensaje de la notificación.
        """
        print(f"Notification to {self.name}: {message}")

# Ejemplo de uso
try:
    # Crea una instancia de SNS
    sns = SNS()
    
    # Crea dos instancias de Endpoint
    email = Endpoint("Email")
    sms = Endpoint("SMS")
    
    # Crea un tema
    topic = sns.create_topic("MyTopic")
    
    # Suscribe los endpoints al tema
    sns.subscribe(topic, email)
    sns.subscribe(topic, sms)
    
    # Publica un mensaje en el tema
    sns.publish(topic, "Hello, world")
except Exception as e:
    # Registra cualquier error que ocurra
    logging.error(f"Error: {e}")
