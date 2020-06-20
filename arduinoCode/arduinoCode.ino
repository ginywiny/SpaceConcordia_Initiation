int LED = 13;

int tempPin = A0; //Set this value to read analog data from temperature sensor
float temp = 0;

void setup() {
  //pinMode(LED, OUTPUT);
  //digitalWrite(LED, LOW);
  Serial.begin(9600);
}

//void digital_read(int pin_number){
//
//    digital_value = digitalRead(pin_number);
//    Serial.print('D');
//    Serial.print(pin_number);
//    Serial.print(':');
//    Serial.println(digital_value);
//}
//
//void analog_read(int pin_number){
//
//    analog_value = analogRead(pin_number);
//    Serial.print('A');
//    Serial.print(pin_number);
//    Serial.print(':');
//    Serial.println(analog_value);
//}


void loop() {

  //Temperature reading
  float tempvoltage = analogRead(tempPin) * 5.0;
  tempvoltage /= 1024.0;
  float tempCel = (tempvoltage - 0.5) * 100;
  Serial.println(tempCel);
  
  if (Serial.available() > 0) {
    if (Serial.read() == 'h') {
      digitalWrite(LED, HIGH);
      Serial.write("Led on");
      //delay(3000);
    }

    if (Serial.read() == 'l') {
      digitalWrite(LED, LOW);
      Serial.write("Led off");
    }
  }

//  else {
//    digitalWrite(LED, LOW);
//  }

  delay(1000);
}
