def sphereVol():
    rad = int(input("Enter the radius of the sphere: "))
    vol = lambda r: (4/3) * 3.14 * pow(r, 3)
    print("Volume of the sphere:", vol(rad))

sphereVol()
