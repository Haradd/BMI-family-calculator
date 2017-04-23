import json


class BMI:

    def __init__(self, height = 160, weight = 50):
        self.height = height
        self.weight = weight

    def take_data(self, parametr):
        return float(input("Give us your  {} ".format(parametr)))

    def count_bmi(self):
        self.bmi_score = self.weight / self.height**2
        return round(self.bmi_score, 2)

    def norm(self, bmi, parametr = 1.0):
        if bmi < 18.5 * parametr:
            return 'underweight'
        elif bmi > 25 * parametr:
            return 'overweight'
        elif bmi > 30 * parametr:
            return 'heavily overweight'
        else:
            return 'at a healthy weight :)'


class Family(BMI):


    def __init__(self):
        self.help()
        try:
            with open('family.json') as file:
                self.members = json.load(file)
        except ValueError:
            self.members = []
        self.command = self.take_command()
        while self.command != 'exit':

            if self.command == 'members':
                self.familly_status()
                self.command = self.take_command()

            elif self.command == 'add':
                member = self.add_member()
                self.members.append(member)
                print('New family member has been added - {0}'.format(member['name']))
                self.command = self.take_command()

            elif self.command.find('.status') != -1:
                name = self.command
                name = name[:len(name) - 7]
                self.person_status(name)
                self.command = self.take_command()

            elif self.command.find('.remove') != -1:
                name = self.command
                name = name[:len(name) - 7]
                self.remove_member(name)
                self.command = self.take_command()

            elif self.command == 'cat':
                self.cat()
                self.command = self.take_command()

            elif self.command == 'dog':
                self.dog()
                self.command = self.take_command()

            elif self.command == 'help':
                self.help()
                self.command = self.take_command()

            elif self.command == 'save':
                self.save()
                self.command = self.take_command()

            else:
                self.command = self.take_command()
        self.exit()

    def save(self):
        with open('family.json', 'w') as file:
            json.dump(self.members, file)

    def take_command(self):
        return input('')

    def help(self):
        print('Type: \n',
              '"members" to check out family members \n',
              '"add" to add new member \n',
              '"Name.status" to check out status of person you want \n',
              '"Name.remove" to remove person from family \n'
              '"cat" to calculate BMI of your cat \n',
              '"dog" to calculate BMI of your dog \n',
              '"help" to remind instructions \n',
              '"save" to save your data \n',
              '"exit" to quit')

    def familly_status(self):
        for person in self.members:
            print(person['name'], 'is', person['height'], 'm height and weigh', person['weight'], 'kg.',
                  'Your BMI: ', person['bmi'], ' - ', 'you are', person['norm'])

    def person_status(self, name):
        for person in self.members:
            if person['name'] == name:
                print(name, 'is', person['height'], 'm height and weigh', person['weight'], 'kg.',
                      'Your BMI: ', person['bmi'], ' - ', 'you are', person['norm'])

    def add_member(self):
        self.name = input("Give us name: ")
        self.height = self.take_data('height (m): ')
        self.weight = self.take_data('weight (kg): ')
        bmi = self.count_bmi()
        return {'name': self.name, 'height': self.height, 'weight': self.weight, 'bmi': bmi, 'norm': self.norm(bmi)}

    def remove_member(self, name):
        new_members = [member for member in self.members if member.get('name') != name]
        if new_members != self.members:
            self.members = new_members[:]
            print(name, 'removed')
        else:
            print('There is no such name')

    def cat(self):
        self.height = self.take_data('cat height (m)')
        self.weight = self.take_data('cat weight (kg)')
        bmi = self.count_bmi()
        print("Your cat's BMI is:", bmi, ' - ', 'he is', self.norm(bmi, 2.25))

    def dog(self):
        self.height = self.take_data('dog height (m)')
        self.weight = self.take_data('dog weight (kg)')
        bmi = self.count_bmi()
        print("Your dog's BMI is:'", bmi, ' - ', 'he is', self.norm(bmi, 1.33))

    def exit(self):
        while 1:
            response = input('do you want to save? (y/n)')
            if response == 'y':
                self.save()
                print('Saved')
                break
            elif response == 'n':
                break
        print('See you later :)')

if __name__ == '__main__':

    Adams = Family()