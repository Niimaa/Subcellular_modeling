
def perturb():
    model = '''
   model event_str
   J1: $X0 -> S1; K1*X0;
   J2: S1 -> $X1; K2*S1;

   X0 = 1; K1 = 0.2; K2 = 0.4; S1 = 0.5;
   E1: at (time > 20): S1 = S1 + 0.35;
   end
   '''
    return model
