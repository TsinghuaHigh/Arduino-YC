const int JoyStick_X = 1;
const int JoyStick_Y = 2;
int flag = 0;

void intFunc()
{
  Serial.println('0');
  Serial.println('0');
  Serial.println('0');
  Serial.println('0');
  Serial.println('0');
}

void check()
{
  int i = analogRead(JoyStick_X);
  int j = analogRead(JoyStick_Y);
  if (i > 500 && i < 600 && j > 500 && j < 600)
  {
    flag = 1;
  }
}

void setup() 
{
  Serial.begin(9600);
  attachInterrupt(0, intFunc, RISING);
}

void loop() 
{
  if (analogRead(JoyStick_X) < 500)
  {
    Serial.println('1');   //RIGHT
    Serial.println('1');
    Serial.println('1');
    Serial.println('1');
    Serial.println('1');
  }
  else if (analogRead(JoyStick_X) > 600)
  {
    Serial.println('2');   //LEFT
    Serial.println('2');
    Serial.println('2');
    Serial.println('2');
    Serial.println('2');
  }
  if (analogRead(JoyStick_Y) < 500)
  {
    Serial.println('3');   //DOWN
    Serial.println('3');
    Serial.println('3');
    Serial.println('3');
    Serial.println('3');
  }
  else if (analogRead(JoyStick_Y) > 600)
  {
    Serial.println('4');   //UP
    Serial.println('4');
    Serial.println('4');
    Serial.println('4');
    Serial.println('4');
  }
  flag = 0;
  for (; flag == 0; )
  {
    check();
    delay(100);
  }
}
