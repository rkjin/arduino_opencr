void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}
int first = 33;
int second = 34;
int third = 35;

void loop() {
  // put your main code here, to run repeatedly:
Serial.println("Hello world");
delay(500);
Serial.write(first); 
Serial.write(second);
Serial.write(third);

Serial.println(first);
Serial.println(second);
Serial.println(third);
}
