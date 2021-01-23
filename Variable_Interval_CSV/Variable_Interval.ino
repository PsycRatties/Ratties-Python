/* Variable Interval (VI) program
   Created: 9/11/2018
   Authors: Daniel W. Anner
*/

int delay_value = 500; // how fast the audible click is (higher=longer)
int fr = 5; // amount of button presses to start the relay
int interval_upper = 10; // highest variable interval that can be selected
int interval_lower = 2; // lowest variable interval that can be selected

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
  }
}

void loop() {
  bool hasRun = false; // simple temp var for do while loop
  int delay_seconds = (random(interval_lower, interval_upper) * 1000); // use ratio limits to get random value
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
