#define TIMER_INTERRUPT_DEBUG      1
#include <SoftwareSerial.h>
#include "ESP8266TimerInterrupt.h"
#include "DHT.h"

#define DHTPIN D5 // pino que estamos conectado
#define DHTTYPE DHT11 // DHT 11
#define LDRPIN A0

DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial loraSerial(D6, D7); // TX, RX

void readAndSend();
float temperaturas[10];
float umidades[10];
int luminosidades[10];
volatile int _index;

void ICACHE_RAM_ATTR TimerHandler(void)
{
  _index = 0;
  float temp = 0.0;
  float umi = 0.0;
  int luz = 0;

  for (int i = 0; i < 10; i++) {
    temp = temp + temperaturas[i];
    umi = umi + umidades[i];
    luz = luz + luminosidades[i];
  }

  Serial.print("Temp: ");
  Serial.print(temp / 10);
  Serial.print("°C\tUmi: ");
  Serial.print(umi / 10);
  Serial.print("% \tLuz: ");
  Serial.println(floor(luz / 10));
  String message = "temp: " + String(temp / 10.0) + "\tumi: " + String(umi / 10.0) + "\tluz: " + String(luz / 10) + "x";
  loraSerial.println(message);
}

#define TIMER_INTERVAL_MS        1000

// Init ESP8266 timer 0
ESP8266Timer ITimer;

void setup()
{

  Serial.begin(115200);
  loraSerial.begin(9600);
  Serial.println("DHTxx test!");

  for (int i = 0; i < 10; i++) {
    temperaturas[i] = 0.0;
    umidades[i] = 0.0 ;
    luminosidades[i] = 0;
  }

  ITimer.attachInterruptInterval(TIMER_INTERVAL_MS * 5000, TimerHandler);

  dht.begin();
}

void loop()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int ldrValue = analogRead(LDRPIN);
  if (_index >= 10) _index = 0;

  if (isnan(t) || isnan(h))
  {
    Serial.println("Failed to read from DHT");
  }
  else
  {
    temperaturas[_index] = t;
    umidades[_index] = h;
    _index++;
  }
  luminosidades[_index] = ldrValue;
  delay(300);
}
