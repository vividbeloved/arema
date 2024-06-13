from flask import Flask, render_template, request

app = Flask(__name__)

class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for entry in self.entries:
                file.write(entry + '\n')

my_journal = Journal()

@app.route('/')
def index():
    return render_template('index.html', entries=my_journal.get_entries())

@app.route('/add_entry', methods=['POST'])
def add_entry():
    entry = request.form['entry']
    my_journal.add_entry(entry)
    return 'Entry added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
