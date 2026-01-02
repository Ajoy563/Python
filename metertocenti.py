meter= float(input("Enter a value in meters: "))
centimeter= float(input("Enter a value in centimeters: "))

meters_to_centimeters= {"meters": meter,"centimeters": meter * 100}
centimeters_to_meters= {"centimeters": centimeter,"meters": centimeter / 100}

print("\nMeters to Centimeters Dictionary:")
for key, value in meters_to_centimeters.items():
    print(f"{key}: {value}")

print("\nCentimeters to Meters Dictionary:")
for key, value in centimeters_to_meters.items():
    print(f"{key}: {value}")