class Diary():
    info = 'diary entry'
    
    def __init__(self, n_entry=0, entries={}):
        self.n_entry = n_entry
        self.entries = entries
    
    def diary_entry(self, entry):
        self.entries.update({(self.n_entry+1):entry})
        self.n_entry+=1

    def diary_page(self, entry_n):
        output = self.entries[entry_n]
        return output


def read_diary(diary_name):
    print(diary_name.entries)


def create_diary():
    name = input('What would you like to call your diary? ')
    name = Diary()
    choice = input("Would you like to add an entry? ")
    if choice == 'yes':
        entry = input('type the entry: ')
        name.diary_entry(entry)
        print('your entry has been added')
    elif choice == 'no':
        print('okay, you can add an entry anytime using the diary_entry method')


