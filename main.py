import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("x" * 50)

entered_num = input("Please enter a phone number: ")

# create PhoneNumber object
phone_num = phonenumbers.parse(entered_num, None)
print(phonenumbers.country_code_for_region(entered_num))
# phone_num = phonenumbers.parse(entered_num, "YE")

print(phone_num)

# You might want to get some information about the location that corresponds to a phone number.
print(geocoder.description_for_number(phone_num, "ar"))
print(geocoder.description_for_number(phone_num, "en"))

# For mobile numbers in some countries,
# you can also find out information about which carrier originally owned a phone number.
print(carrier.name_for_number(phone_num, "en"))


# You might also be able to retrieve a list of time zone names that the number potentially belongs to.
print(timezone.time_zones_for_number(phone_num))
