from flask import Flask, render_template, request
from sudoku import generate_board, check_solution

app = Flask(__name__)
game_board = generate_board()

@app.route('/')
def index():
    return render_template('sudoku.html', board=game_board)

@app.route('/submit', methods=['POST'])
def submit():
    user_board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = request.form.get(f'cell-{i}-{j}')
            try:
                row.append(int(val))
            except:
                row.append(0)
        user_board.append(row)

    result = check_solution(user_board)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)

