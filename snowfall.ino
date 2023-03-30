int xyzPins[] = {13, 12, 17};  //x,y,z pins
int b = 1;
int lastState = HIGH; // the previous state from the input pin
int currentState;   

void setup() {
  Serial.begin(9600);
  pinMode(xyzPins[2], INPUT_PULLUP);  //z axis is a button.
  pinMode(21, INPUT_PULLUP);  //button.
}
void loop() {
  int xVal = analogRead(xyzPins[0]);
  int yVal = analogRead(xyzPins[1]);
  int zVal = digitalRead(xyzPins[2]);
  currentState = digitalRead(21);

  if(lastState == LOW && currentState == HIGH){
    // Serial.println("The state changed from LOW to HIGH");
    b = 0;
  }
  lastState = currentState;
  // Serial.print(buttonVal);
  Serial.printf("%d, %d, %d, %d", xVal, yVal, zVal, b);
  b = 1;
  Serial.print('\n');
  delay(100);
}