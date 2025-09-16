#include <DHT.h>
#include <Servo.h>

#define DHTPIN 2
#define DHTTYPE DHT11
const int pinoServo = 5;
const int buzzer = 9;
const int botao = 7;

DHT dht(DHTPIN, DHTTYPE);
Servo servo;

void setup() {
  Serial.begin(9600);
  dht.begin();
  servo.attach(pinoServo);
  pinMode(buzzer, OUTPUT);
  pinMode(botao, INPUT_PULLUP);
}

void loop() {
  float temperatura = dht.readTemperature();

  if (isnan(temperatura)) {
    Serial.println("Erro ao ler DHT11!");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");

  if (digitalRead(botao) == LOW) {
    servo.write(180);
    noTone(buzzer);
    Serial.println("Modo manual: ventilação aberta total");
    delay(500);
    return;
  }

  int angulo = 0;
  if (temperatura < 20) {
    angulo = 0;
  } else if (temperatura < 25) {
    angulo = 45;
  } else if (temperatura < 30) {
    angulo = 90;
  } else if (temperatura < 35) {
    angulo = 135;
  } else {
    angulo = 180;
  }

  servo.write(angulo);

  if (temperatura < 15 || temperatura > 40) {
    tone(buzzer, 1000);
  } else {
    noTone(buzzer);
  }

  delay(2000);
}