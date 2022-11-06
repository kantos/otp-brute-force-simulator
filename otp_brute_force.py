import secrets
import random

attempts_per_otp = 5
window_length_minutes = 3
attack_days = 180
otp_creations = int(60/window_length_minutes)*24*attack_days
simulations = 100
users = 1
otp_length = 6
otp_type = "numeric"
valid_otp_window = 10
otp_max_size = 10**otp_length

def create_otp():
    if otp_type == "numeric":
        otp = secrets.randbelow(otp_max_size)
        #otp = random.randrange(otp_max_size)

    #TO DO else
    return otp

    
def window_brute_force():
    for i in range(valid_otp_window):
        otp = create_otp()
        #print(otp)
        if otp >= 0 and otp < attempts_per_otp:
            return True

    return False


def otp_brute_force():
    for i in range(otp_creations):
        if window_brute_force():
            return True

    return False

def simulate():
    successful = 0
    for i in range(simulations * users):
        if otp_brute_force():
            successful += 1
    avg = successful / (simulations * users)
    print("Simulations: " +str(simulations)+ "\nOTP windows: " +str(otp_creations)+ "\nOTP length:" + str(otp_length) + "\nProbability of success: " + str(avg)) 

simulate()