/* Variable Interval (VI) program
   Created: 9/11/2018
   Authors: Daniel W. Anner
*/

int delay_value = 500; // how fast the audible click is (higher=longer)
int interval_upper = 30; // highest time interval that can be selected
int interval_lower = 10; // lowest time interval that can be selected
int timesToClick = 5; // amount of times the relay should be triggered (default: 10)

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

  for (int i = 0; i < timesToClick; i++) { //repeat the next if/else 10 times
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
  int delay_seconds = (random(interval_lower, interval_upper) * 1000); // use ratio limits to get random value
  digitalWrite(3, LOW); digitalWrite(6, LOW); // turn off both LED's on start of script

  do {
    delay(delay_seconds); // delay given time
    if (digitalRead(8) == HIGH) { triggerRelay(); } else return; // ensure the green button is pressed, then trigger relay
    delay_seconds = (random(interval_lower, interval_upper) * 1000); // use ratio limits to get random value
  } while (digitalRead(8) == HIGH); // do this while the green button is pressed
}
