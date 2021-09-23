# name of student:      // Diemaco
# number of student:    // 99065776
# purpose of program:   // Calculate the amount of change needed to be returned
# function of program:  // ^
# structure of program: //

# All of the coins and their value in an array
coinsWorth = [500, 300, 200, 50, 20, 10, 5, 2, 1]

# Array for storing the amount of coins return by the user
coinsAmount = [0] * len(coinsWorth)

# Get the amount to be paid in cents
toPay = int(float(input('Amount to pay: ')) * 100)

# Get the amount of cents paid
paid = int(float(input('Paid amount: ')) * 100)

# Calculate the amount to be returned to the buyer
change = paid - toPay

# If there's any change continue
if change > 0:

    # While there is something that needs to be returned and we haven't ran out of coins
    for coin in range(len(coinsWorth)):

        # Get the amount of coins the user can return
        nrCoinsToReturn = change // coinsWorth[coin]

        # Only print if the amount of coins the user can return is above 0
        if nrCoinsToReturn > 0:

            # Print how much the user can return
            print(f'\n\nYou can return a maximum of {nrCoinsToReturn:,} worth €{coinsWorth[coin] / 100:,.2f} cents per coin')

            # Get from the user how much he has returned
            nrCoinsReturned = int(input(f'How many coins of {coinsWorth[coin]} cent(s) did you return? \n'))

            # Store the amount of coins returned for later use
            coinsAmount[coin] = nrCoinsReturned

            # Decrease the amount of change by the amount of change actually returned
            change -= nrCoinsReturned * coinsWorth[coin]

    # Print the amount of coins returned by the user (per coin)
    for coin in range(len(coinsWorth)):
        print(f'You returned a total of {coinsAmount[coin]} coins worth {coinsWorth[coin]} cents per coin')

    # If there is still some change that needs to returned print the amount to the user (in euros)
    if change > 0:
        print(f'Change not returned: €{change / 100:,.2f}')
else:
    print('No change needs to be returned!')
