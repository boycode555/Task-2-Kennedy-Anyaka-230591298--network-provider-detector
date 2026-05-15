def detect_network(number):

    prefixes = {
        "MTN": ["0803", "0806", "0703", "0813"],
        "AIRTEL": ["0802", "0808", "0708", "0812"],
        "GLO": ["0805", "0807", "0705", "0815"],
        "9MOBILE": ["0809", "0817", "0818"]
    }

    prefix = number[:4]

    for network, nums in prefixes.items():
        if prefix in nums:
            return network

    return "Unknown Network"


phone = input("Enter Phone Number: ")

if len(phone) != 11 or not phone.isdigit():
    print("Invalid Phone Number")
else:
    result = detect_network(phone)
    print("Network Provider:", result)

