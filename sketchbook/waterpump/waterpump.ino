int AA = 5;
int AB = 6;

void setup() {
  pinMode(AA, OUTPUT);
  pinMode(AB, OUTPUT);
}

void loop() {
  digitalWrite(AA, HIGH);
  digitalWrite(AB, LOW);
  delay(3000);
  digitalWrite(AA, LOW);
  digitalWrite(AB, LOW);
  delay(3000);
  exit(0);
  
}

