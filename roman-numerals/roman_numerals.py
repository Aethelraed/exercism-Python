def roman(number):
    return str(number * "I").replace(1000*"I","M").replace(500*"I","D").replace(100*"I","C").replace(50*"I","L").replace(10*"I","X").replace(5*"I","V").replace(4*"I","IV").replace(4*"X","XL").replace(4*"C","CD").replace("VIV","IX").replace("LXL","XC").replace("DCD","CM")

