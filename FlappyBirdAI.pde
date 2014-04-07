void setup()
{
  Serial.begin(9600);
  attachInterrupt(0, intFunc, RISING);
}

void loop()
{
  delay(10000);
}

void intFunc()
{
  Serial.println('1');
}
