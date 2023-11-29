int AA = 5;
int AB = 6;

void setup()  {
  
  Serial.begin(9600);
  pinMode(AA, OUTPUT);
  pinMode(AB, OUTPUT);
  
}


void loop() {
  int humidity = analogRead(A0);
  int humi = map(humidity,1023,400,0,100);
  
  
  if(humi <= 50)
  {
  
  Serial.print("humidity : ");
  Serial.println(humi);
  delay(1000);
  digitalWrite(AA, HIGH);
  digitalWrite(AB, LOW);
  delay(1000);
  digitalWrite(AA, LOW);
  digitalWrite(AB, LOW);
  delay(1000);
  }
  else
  {
  Serial.print("humidity : ");
  Serial.println(humi);
  delay(1000);
  }
  
}
