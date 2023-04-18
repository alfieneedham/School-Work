from math import sqrt

children = [(9, 9),(11, 12),(13, 15),(1, 0)]
marble = (10, 10)


closestCollisionPoint = (100, None)
for child in children:
    xDistanceSquared = ((child[0]-marble[0]))
    yDistanceSquared = ((child[1]-marble[1]))
    #distanceToPinball = sqrt(xDistanceSquared + yDistanceSquared)
    print(child, xDistanceSquared, str(xDistanceSquared*xDistanceSquared), yDistanceSquared, )
#     if distanceToPinball < closestCollisionPoint[0]:
#         closestCollisionPoint = (distanceToPinball, child)
# print(closestCollisionPoint)