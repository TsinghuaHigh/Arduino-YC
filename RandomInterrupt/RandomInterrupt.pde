volatile int flag = 0;
const int lightCtrl[10][8] =
{
  {1,1,1,0,1,1,1,0},
  {0,0,1,0,1,0,0,0},
  {1,1,0,0,1,1,0,1},
  {0,1,1,0,1,1,0,1},
  {0,0,1,0,1,0,1,1},
  {0,1,1,0,0,1,1,1},
  {1,1,1,0,0,1,1,1},
  {0,0,1,0,1,1,0,0},
  {1,1,1,0,1,1,1,1},
  {0,1,1,0,1,1,1,1},
};

void setup()
{
  for (int i = 0; i < 8; ++i)
  {
    pinMode(i + 5, OUTPUT);
  }
  attachInterrupt(0, intFunc, RISING);
}

void intFunc()
{
  flag = !flag;
}

void light(int rand)
{
  for (int i = 0; i < 8; ++i)
  {
    if (lightCtrl[rand][i] == 1)
    {
      digitalWrite(i + 5, LOW);
    }
  }
}

void loop()
{
  for (;flag == 1;)
  {
    delay(100);
  }
  for (int i = 0; i < 8; ++i)
  {
    digitalWrite(i + 5, HIGH);
  }
  light(random() % 10);
  if (flag == 0)
  {
    delay(100);
  }
}
