#include <DHT.h>
#include <ESP8266WiFi.h>
#include <ThingSpeak.h>

// WiFi Configuration
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// ThingSpeak Configuration
unsigned long channelID = YOUR_CHANNEL_ID;
const char* writeAPIKey = "YOUR_WRITE_API_KEY";
const char* readAPIKey = "YOUR_READ_API_KEY";

// Hardware Configuration
#define DHTPIN D1          // DHT11 data pin
#define LIGHT_PIN D2       // Relay for light control
#define FAN_PIN D3         // Relay for fan control
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(100);
  
  // Initialize hardware
  pinMode(LIGHT_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  digitalWrite(LIGHT_PIN, LOW);
  digitalWrite(FAN_PIN, LOW);
  
  dht.begin();
  
  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected!");
  
  ThingSpeak.begin(client);
}

void loop() {
  // Read sensor data
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  // Validate readings
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read DHT sensor!");
    delay(2000);
    return;
  }
  
  // Read control states from ThingSpeak
  int lightState = ThingSpeak.readFloatField(channelID, 3, readAPIKey);
  int fanState = ThingSpeak.readFloatField(channelID, 4, readAPIKey);
  
  // Update device states
  digitalWrite(LIGHT_PIN, (lightState == 1) ? HIGH : LOW);
  digitalWrite(FAN_PIN, (fanState == 1) ? HIGH : LOW);
  
  // Send data to ThingSpeak
  ThingSpeak.setField(1, temperature);
  ThingSpeak.setField(2, humidity);
  ThingSpeak.setField(3, digitalRead(LIGHT_PIN));
  ThingSpeak.setField(4, digitalRead(FAN_PIN));
  
  int statusCode = ThingSpeak.writeFields(channelID, writeAPIKey);
  
  if (statusCode == 200) {
    Serial.println("Data sent to ThingSpeak!");
    Serial.print("Temperature: "); Serial.print(temperature); Serial.println("°C");
    Serial.print("Humidity: "); Serial.print(humidity); Serial.println("%");
    Serial.print("Light: "); Serial.println(lightState ? "ON" : "OFF");
    Serial.print("Fan: "); Serial.println(fanState ? "ON" : "OFF");
  } else {
    Serial.println("Failed to send data. Error: " + String(statusCode));
  }
  
  // Respect ThingSpeak's 15s update limit
  delay(20000);
}
