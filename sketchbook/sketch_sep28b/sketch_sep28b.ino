
const int sw = 4;
void setup() {

//핀 모드 설정

  pinMode(sw, OUTPUT);
}

void loop() {
  int fanOnTime =  5000;
  int fanOffTime = 3000;
  
  digitalWrite(sw,HIGH);
  delay(fanOnTime);
  
  digitalWrite(sw,LOW);
  delay(fanOffTime);
  exit(0);
}

 
