void setup()

{

  pinMode(A1, INPUT); //A0아날로그핀을 입력으로 사용함

  Serial.begin(9600); //시리얼 모니터 출력을 위해 시리얼 통신 값을 정해줌

}



void loop()

{

  Serial.println(analogRead(A1)); //시리얼 모니터에 아날로그 A0의 값을 보여줌

  delay(500); 					  //0.5초의 딜레이를 줌(모니터에 출력되는 값을 천천히 읽기 위해)

}

