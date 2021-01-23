/* Fixed Interval (FI) program
   Created: 9/10/2018
   Modified: 9/11/2018
   Authors: Daniel W. Anner
*/

int delay_value = 500; // how fast the audible click is (higher=longer)
int fr = 5; // amount of button presses to start the relay
int switchcounter2 = 0; // counter for small button presses
int delay_seconds = 10; // seconds to delay the dispense button activation

void setup() {
  pinMode(2, INPUT); // right switch (spst momentary n.o.)
  pinMode(3, OUTPUT);  // LED red middle
  pinMode(4, INPUT);  // right switch, bottom black (spst)
  pinMode(5, OUTPUT);  // LED left blue
  pinMode(6, OUTPUT);  // LED right green
  pinMode(7, INPUT);  // left switch (spst momentary n.o.)
  pinMode(8, INPUT);  // left switch, bottom green (spst)
  pinMode(10, OUTPUT);  // relay

  delay_seconds = (delay_seconds * 1000); // convert "seconds" to milliseconds
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
  bool hasRun = false; // simple temp var for do while loop
  digitalWrite(3, LOW); digitalWrite(6, LOW); // turn off both LED's on start of script

  if (digitalRead(4) == HIGH) { //Bottom BLACK Button
    digitalWrite(6, digitalRead(4)); //Turn on the GREEN light

    delay(delay_seconds); 

    do {
      if (digitalRead(2) == HIGH) { hasRun = true; triggerRelay(); }
    } while (!hasRun);
  } else if (digitalRead(8) == HIGH) { //Bottom GREEN Button
    digitalWrite(3, digitalRead(8)); //Turn on the RED light

    delay(delay_seconds); 

    do {
      if (digitalRead(7) == HIGH) { hasRun = true; triggerRelay(); }
    } while (!hasRun);
  } else { digitalWrite(3, LOW); digitalWrite(6, LOW); }
}
