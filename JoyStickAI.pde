const int JoyStick_X = 1;
const int JoyStick_Y = 2;

void setup() 
{
  Serial.begin(9600);
}
void loop() 
{
  if (analogRead(JoyStick_X) < 500)
  {
    Serial.println('0');   //RIGHT
  }
  else if (analogRead(JoyStick_X) > 600)
  {
    Serial.println('1');   //LEFT
  }
  if (analogRead(JoyStick_Y) < 500)
  {
    Serial.println('2');   //DOWN
  }
  else if (analogRead(JoyStick_Y) > 600)
  {
    Serial.println('3');   //UP
  }
  delay(100);
}
