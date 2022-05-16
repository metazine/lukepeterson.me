import re

def main():
    phoneNumberRegex = re.compile(r"07\d\d\d \d\d\d \d\d\d")
    mo = phoneNumberRegex.search("Hello there my name is Luke and my phone number is 07426 182 402 isn't that so cool! 07345 678 910")
    print("Phone number found: " + mo.group())
    mo = phoneNumberRegex.findall("Hello there my name is Luke and my phone number is 07426 182 402 isn't that so cool! 07345 678 910")
    print(mo)

    batRegex = re.compile(r"(Bat(man|woman|mobile|arang))")
    mo = batRegex.findall("""Damn Batman well done recruiting Batwoman. I have to apologise but I threw a Batarang at the wheel of the Batmobile""")

    batmanStr = ""
    for item in mo:
        batmanStr += item[0] + " "
    print(batmanStr)

if __name__ == "__main__":
    main()