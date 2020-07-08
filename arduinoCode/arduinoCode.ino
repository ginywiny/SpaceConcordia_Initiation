int LED = 13;
int tempPin = A0; //Set this value to read analog data from temperature sensor
float temp = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void(* resetFunc) (void) = 0;

void loop() {

  //Temperature reading
  float tempvoltage = analogRead(tempPin) * 5.0;
  tempvoltage /= 1024.0;
  float tempCel = (tempvoltage - 0.5) * 100;
  Serial.println(tempCel);
  
  if (Serial.available() > 0) {
    
    if (Serial.read() == 'h') {
      digitalWrite(LED, HIGH);
      //delay(2000);
    }

    else {
        digitalWrite(LED, LOW);
        resetFunc();
      //delay(2000);
    }
  }
  delay(1500);
}
