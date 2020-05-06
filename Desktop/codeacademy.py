def f_to_c(f_temp , c_temp):
  c_temp = f_temp - 32 * 5/9
  return c_temp
  print(c_temp)
f100_in_celsius = f_to_c(f_temp = 100, c_temp = 0)
def c_to_f(c_temp , f_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
  print(f_temp)
c0_in_fahrenheit = c_to_f(c_temp = 0 , f_temp = 0)

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(train_mass , train_acceleration):
  force = train_mass * train_acceleration
  return force
  print(force)

get_force(train_mass = 100 , train_acceleration = 10)
c_to_f(c_temp = 15 , f_temp = 10)