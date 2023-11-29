




#include <Adafruit_Sensor.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <Adafruit_Sensor.h>
#include "DHT.h"




DHT dht(8, DHT22); /*8번 PIN에서 데이터가 들어오고, 
                     센서는 DHT22 센서를 사용한다고 정의합니다.
                     */                    
int AA = 5;
int AB = 6;                     
 
void setup() {
  
  
  
  pinMode(A1, INPUT); //A0아날로그핀을 입력으로 사용함
  
  Serial.begin(9600); //PC모니터를 이용하기 위하여, 
  
  pinMode(AA, OUTPUT);
  pinMode(AB, OUTPUT);

  pinMode(13, OUTPUT);
  dht.begin(); //DHT22센서의 사용시작을 정의해줍니다.

}
 
void loop() {
// 센서에서 데이터 읽기

  int sensorValue = analogRead(A0);
  // 데이터를 문자열로 형식화

  String data = String(sensorValue);
  // 데이터를 라즈베리 파이로 전송

  Serial.println(data);
 
  float h = dht.readHumidity();  //습도값을 읽어옴. 
  float t = dht.readTemperature(); //온도값을 읽어옴
  int cdsValue = analogRead(A1);
  int humidity = analogRead(A0);
  int humi = map(humidity,1023,400,0,100);
  
  Serial.print(h); //습도가 출력 됩니다.
  Serial.print(",");
  Serial.print(t); //온도가 출력됩니다.
  Serial.print(",");
  Serial.print(cdsValue); //시리얼 모니터에 아날로그 A0의 값을 보여줌
  Serial.print(",");
  Serial.println(humi);



  if(t>22.00)
  {
    digitalWrite(13,HIGH);
  }
  else
  {
    digitalWrite(13,LOW);
  }
  
  if(humi < 0)
  {
  

  delay(1000);
  digitalWrite(AA, HIGH);
  digitalWrite(AB, LOW);

  }
  else
  {
  digitalWrite(AA, LOW);
  digitalWrite(AB, LOW);
  }
  



  delay(1000);

  
 
}

