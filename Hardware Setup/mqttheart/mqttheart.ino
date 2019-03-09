#include <ESP8266WiFi.h>
#include <MQTT.h>

const char ssid[] = "Guest";
const char pass[] = "C0rp$Gu3sT!";
int sensorPin = A0;
double alpha = 0.75;
int period = 100;
double change = 0.0;
double minval = 0.0;
WiFiClient net;
MQTTClient client;

unsigned long lastMillis = 0;

void connect() {
  Serial.print("checking wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  Serial.print("\nconnecting...");
  while (!client.connect("arduino", "try", "try")) {
    Serial.print(". ");
    delay(1000);
  }

  Serial.println("\nconnected!");

  client.subscribe("#");
  // client.unsubscribe("/hello");
}

void messageReceived(String &topic, String &payload) {
  Serial.println("incoming: " + topic + " - " + payload);
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);

  // Note: Local domain names (e.g. "Computer.local" on OSX) are not supported by Arduino.
  // You need to set the IP address directly.
  client.begin("10.177.7.168", net);
  client.onMessage(messageReceived);

  connect();
}

void loop() {
  client.loop();
  delay(10);  // <- fixes some issues with WiFi stability

  if (!client.connected()) {
    connect();
  }

  // publish a message roughly every second.
  if (millis() - lastMillis > 3000) {
        static double oldValue = 0;
    static double oldChange = 0;
 
    int rawValue = analogRead (sensorPin);
    double value = alpha * oldValue + (1 - alpha) * rawValue;
 
   Serial.println (value);
    oldValue = value;
 
    lastMillis = millis();
    client.publish("heart",String((value),2));
    long c=random(80,100);
        client.publish("temp",String(c));
        c=random(100,140);
    client.publish("bp",String(c));


  }
}
