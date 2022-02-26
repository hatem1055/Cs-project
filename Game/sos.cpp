#include <iostream>
#include <vector>
#include <cmath>
#include <cctype>

using namespace std;
vector<vector<string>> create_basic_board(int dimensions){
    vector<vector<string>> board {};
    int n {1};
    for (int i {0}; i < dimensions ; i++){
        vector<string> row {};
        for (int j {0}; j < dimensions ; j++){
            row.push_back(to_string(n));
            n += 1;
        }
        board.push_back(row);
    }
    return board;
};
void draw_board(vector<vector<string>> board){
    string result {""};
    for(vector<string> row : board){
        for (string cell : row){
            if (cell.length() == 1){
                cell = cell == "S" || cell == "O" ? " " + cell : "0" + cell;
            }
            result += "| " + cell + " |";
        }
        result += "\n";
        
    }
    cout << result << endl;
}
vector<int> get_index_from_number(int dimensions,int number){
    if (number <= dimensions){
        return {0,number - 1};
    }
    int row = number % dimensions == 0 ? floor(number / dimensions) : floor(number / dimensions) - 1;
    int column = number % dimensions != 0 ? (number % dimensions) - 1 : dimensions - 1;
    return {row,column};
}
bool validate_input(int dimensions,vector<vector<string>> board, int number){
    if (number > dimensions * dimensions or number <= 0 ){
        return false;
    }
    int row {get_index_from_number(dimensions,number)[0]};
    int column {get_index_from_number(dimensions,number)[0]};
    string cell {board[row][column]};
    return cell != "S" and cell != "O";

}
vector<int> take_input(int dimensions,vector<vector<string>> board,string msg){
    int number {0};
    cout << msg;
    cin >> number;
    while (not(validate_input(dimensions,board,number))){
        cout << "Invalid Input" << endl;
        cout << msg;
        cin >> number;
    }
    return get_index_from_number(dimensions,number);
}
void game(int dimensions){
    vector<vector<string>> board {create_basic_board(dimensions)};
    int available_blocks {dimensions * dimensions};
    draw_board(board);
    int turn {1};
    vector<int> scores {0,0};
    while(available_blocks != 0 ){
        string msg {"Player " + to_string(turn) + "Enter Number : "};
        vector<int> row_column {take_input(dimensions,board,msg)};
        int row {row_column[0]};
        int column {row_column[1]};
        char answere {};
        cout << "Enter S or O : ";
        cin >> answere;
        while(toupper(answere) != 'S' and toupper(answere) != 'O'){
            cout << "Enter S or O : ";
            cin >> answere;
        }
        board[row][column] = toupper(answere);
        draw_board(board);
    }
}
int main(){
    int dimensions {3};
    cout << "dimensions of the board [3-9] : ";
    cin >> dimensions;
    while (dimensions < 3 or dimensions > 9){
        cout << "dimensions of the board [3-9] : ";
        cin >> dimensions;
    }
    game(dimensions);
    system("pause");
    return 0;
}