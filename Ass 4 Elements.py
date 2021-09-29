LEMENTS = (('0', 'Nothing', 'None', '0'), ('1', 'Hydrogen', 'H', '1.007'), ('2', 'Helium', 'He', '4.002'),
            ('3', 'Lithium', 'Li', '6.941'), ('4', 'Beryllium', 'Be', '9.012'), ('5', 'Boron', 'B', '10.811'),
            ('6', 'Carbon', 'C', '12.011'), ('7', 'Nitrogen', 'N', '14.007'), ('8', 'Oxygen', 'O', '15.999'),
            ('9', 'Fluorine', 'F', '18.998'), ('10', 'Neon', 'Ne', '20.18'), ('11', 'Sodium', 'Na', '22.99'),
            ('12', 'Magnesium', 'Mg', '24.305'), ('13', 'Aluminum', 'Al', '26.982'), ('14', 'Silicon', 'Si', '28.086'),
            ('15', 'Phosphorus', 'P', '30.974'), ('16', 'Sulfur', 'S', '32.065'), ('17', 'Chlorine', 'Cl', '35.453'),
            ('18', 'Argon', 'Ar', '39.948'), ('19', 'Potassium', 'K', '39.098'), ('20', 'Calcium', 'Ca', '40.078'),
            ('21', 'Scandium', 'Sc', '44.956'), ('22', 'Titanium', 'Ti', '47.867'), ('23', 'Vanadium', 'V', '50.942'),
            ('24', 'Chromium', 'Cr', '51.996'), ('25', 'Manganese', 'Mn', '54.938'), ('26', 'Iron', 'Fe', '55.845'),
            ('27', 'Cobalt', 'Co', '58.933'), ('28', 'Nickel', 'Ni', '58.693'), ('29', 'Copper', 'Cu', '63.546'),
            ('30', 'Zinc', 'Zn', '65.38'), ('31', 'Gallium', 'Ga', '69.723'), ('32', 'Germanium', 'Ge', '72.64'),
            ('33', 'Arsenic', 'As', '74.922'), ('34', 'Selenium', 'Se', '78.96'), ('35', 'Bromine', 'Br', '79.904'),
            ('36', 'Krypton', 'Kr', '83.798'), ('37', 'Rubidium', 'Rb', '85.468'), ('38', 'Strontium', 'Sr', '87.62'),
            ('39', 'Yttrium', 'Y', '88.906'), ('40', 'Zirconium', 'Zr', '91.224'), ('41', 'Niobium', 'Nb', '92.906'),
            ('42', 'Molybdenum', 'Mo', '95.96'), ('43', 'Technetium', 'Tc', '98'), ('44', 'Ruthenium', 'Ru', '101.07'),
            ('45', 'Rhodium', 'Rh', '102.906'), ('46', 'Palladium', 'Pd', '106.42'), ('47', 'Silver', 'Ag', '107.868'),
            ('48', 'Cadmium', 'Cd', '112.411'), ('49', 'Indium', 'In', '114.818'), ('50', 'Tin', 'Sn', '118.71'))

# This program enables the user to know about a certain element
# We will do so by denoting the element number
# As the input variable
# Here it is
number = 1

# Now we need some rules
# And then the loop! The number that decides if the input
#Is within the range from 1 to 50
choice = 1

while (choice == 1):
    num = int(input("\nPlease Enter the element number : "))

    # This is important! If the element number is not from 1 to 50
    # You won't be able to know about your element!
    if (num < 1 or num > 50):
        print("Error ! Please enter a number in the range 1 - 50.\n")

    else:
        print("{} ({}) with an Atomic mass of {} \n".format(elements[num - 1][2], elements[num - 1][1],
                                                            elements[num - 1][3]))

    print("Would you like to know about another element?")
    print("1 for yes,2 for no")
    choice = int(input())
    if (choice != 1):











