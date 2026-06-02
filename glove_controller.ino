#include <LiquidCrystal.h>
LiquidCrystal lcd(3, 4, 5, 6, 7, 8);

void setup() {
  Serial.begin(115200);
  lcd.begin(16, 2);
  lcd.print("Glove System");
  lcd.setCursor(0, 1);
  lcd.print("Ready to Sync...");
  delay(2000);
  lcd.clear();
}

void loop() {
  int f[5];
  for(int i=0; i<5; i++) {
    f[i] = analogRead(i); 
  }

  Serial.print(f[0]); Serial.print(",");
  Serial.print(f[1]); Serial.print(",");
  Serial.print(f[2]); Serial.print(",");
  Serial.print(f[3]); Serial.print(",");
  Serial.println(f[4]);


  lcd.setCursor(0, 0);
  lcd.print("S:"); 
  for(int i=0; i<5; i++) {
    int shortVal = map(f[i], 0, 1023, 0, 99); 
    if(shortVal < 10) lcd.print("0");
    lcd.print(shortVal);
    if(i < 4) lcd.print("."); 
  }

  if (Serial.available() > 0) {
    String result = Serial.readStringUntil('\n');
    result.trim(); 

    lcd.setCursor(0, 1);
    lcd.print("Ans:            "); 
    lcd.setCursor(5, 1);
    lcd.print(result);             
  }

  delay(100); 
}


String formatVal(int val) {
  if (val < 10) return "  " + String(val);
  if (val < 100) return " " + String(val);
  return String(val);
}





