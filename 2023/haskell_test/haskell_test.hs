double :: Integer -> Integer
double x = (x * 2)

cube :: Integer -> Integer
cube y = (y * y * y)

cubedouble :: Integer -> Integer
cubedouble z = cube(double(z))