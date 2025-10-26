// C++ code
//
int boton = 0;

int valor = 0;

int tiempo = 0;

void setup()
{
  pinMode(2, INPUT);
  pinMode(A0, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  boton = digitalRead(2);
  if (boton == 0) {
    while (1 == 1) {
      valor = analogRead(A0);
      if (valor >= 512) {
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println(valor);
      } else {
        delay(250); // Wait for 250 millisecond(s)
        digitalWrite(LED_BUILTIN, HIGH);
        delay(250); // Wait for 250 millisecond(s)
        digitalWrite(LED_BUILTIN, LOW);
      }
      delay(1000); // Wait for 1000 millisecond(s)
    }
  }
}