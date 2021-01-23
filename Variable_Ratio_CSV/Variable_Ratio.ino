/* Variable Ratio (VR) program
   Same as Fixed Ratio, but altered to have a variable number of button clicks
   Created: 9/7/2018
   Authors: Albena Ammann, Ed Berg, Mark Berg, Daniel W. Anner
*/

int delay_value = 500; // how fast the audible click is (higher=longer)
int switchcounter2 = 0; // counter for small button presses
int ratio_upper = 10; // highest variable ratio that can be selected
int ratio_lower = 2; // lowest variable ratio that can be selected

void setup() {
  pinMode(2, INPUT); // right switch (spst momentary n.o.)
  pinMode(3, OUTPUT);  // LED red middle
  pinMode(4, INPUT);  // right switch, bottom black (spst)
  pinMode(5, OUTPUT);  // LED left blue
  pinMode(6, OUTPUT);  // LED right green
  pinMode(7, INPUT);  // left switch (spst momentary n.o.)
  pinMode(8, INPUT);  // left switch, bottom green (spst)
  pinMode(10, OUTPUT);  // relay
}

void triggerRelay() {
  digitalWrite(6, LOW); //Turn off the GREEN light
  digitalWrite(3, LOW); //Turn off the RED light

  for (int i = 0; i < 10; i++) { //repeat the next if/else 10 times
    digitalWrite(5, LOW);
    digitalWrite(10, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(10, HIGH);
    delay(delay_value);
    digitalWrite(10, LOW);
    delay(delay_value);
    digitalWrite(10, HIGH);
    digitalWrite(10, LOW);
    digitalWrite(5, LOW);
    switchcounter2 = 0;
  }
}

void loop() {
  int switchState2, switchState7;
  int lastswitchstate2 = 0, lastswitchstate7 = 0;
  digitalWrite(3, LOW); digitalWrite(6, LOW);

  int vr = random(ratio_lower, ratio_upper); // use ratio limits to get random value

  if (digitalRead(4) == HIGH) { //Bottom BLACK Button
    digitalWrite(6, digitalRead(4)); //Turn on the GREEN light

    do {
      switchState2 = digitalRead(2); //Read the state of the button
      if ((switchState2 != lastswitchstate2) and (switchState2 == HIGH)) {
        switchcounter2++;  //Increment the counter
      }
      delay(50); //Delay for 50ms
      lastswitchstate2 = switchState2; //store last state (for reset)
    } while (switchcounter2 < vr); //Run this do, while the counter is LESS THAN the variable ratio

    triggerRelay();
    return;
  } else if (digitalRead(8) == HIGH) { //Bottom GREEN Button
    digitalWrite(3, digitalRead(8)); //Turn on the RED light

    do {
      switchState7 = digitalRead(7); //Read the state of the button
      if ((switchState7 != lastswitchstate7) and (switchState7 == HIGH)) {
        switchcounter2++;  //Increment the counter
      }
      delay(50); //Delay for 50ms
      lastswitchstate7 = switchState7; //store last state (for reset)
    } while (switchcounter2 < vr); //Run this do, while the counter is LESS THAN the variable ratio

    triggerRelay();
    return;
  } else { digitalWrite(3, LOW); digitalWrite(6, LOW); }
}
