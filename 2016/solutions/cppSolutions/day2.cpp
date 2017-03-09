//
// Created by Jarek Wojciechowski on 3/8/17.
//

#include "day2.h"
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <unordered_set>

class Keypad{
    std::pair<int,int> xy_location;
    char keypad_grid[5][5] ={{'0','0','0','0','0'},
                             {'0','1','2','3','0'},
                             {'0','4','5','6','0'},
                             {'0','7','8','9','0'},
                             {'0','0','0','0','0'}};
    std::vector<char> final_input;

public:
    Keypad(){ }

    void move_on_keypad(char direction){
        //Get new movement location
        std::pair<int,int> temp_location = xy_location;
        switch(direction){
            case 'U':
                temp_location.first += 1;
                break;
            case 'D':
                temp_location.first -= 1;
                break;
            case 'R':
                temp_location.second += 1;
                break;
            case 'L':
                temp_location.second -= 1;
                break;
            default:
                std::cout << "Invalid movement direction";
                break;
        }
        //Check if out of bounds
        if(keypad_grid[temp_location.first][temp_location.second] != 0){
            //Move to location if within bounds
            xy_location = temp_location;
        }

    }
    void finalize_keyboard_location(){ final_input.push_back(keypad_grid[xy_location.first][xy_location.second]); }

    std::vector<char> get_final_combination(){
        //Probably need to concatenate this into a string
        return final_input;
    }
    void process_character(char in_char) {
        switch(in_char){
            case 'R':
            case 'L':
            case 'U':
            case 'D':
                move_on_keypad(in_char);
            case '\n':
                finalize_keyboard_location();
            default:
                std::cout << "invalid character input";
        }
    }

};


int solve_day2(){
    Keypad keypad = Keypad();

    FILE *fp;
    if( (fp = fopen("day2input.txt", "r+")) == NULL) { printf("File doesn't exist\n"); exit(1); }

    char move_direction;

    fscanf(fp, "%c", &move_direction);

    while(fscanf(fp, "%c", &move_direction) == 1)
        keypad.process_character(move_direction);

    std::vector<char> part1_answer = keypad.get_final_combination();
    std::cout << "Keypad combination: ";
    for (std::vector<char>::const_iterator i = part1_answer.begin(); i != part1_answer.end(); ++i)
        std::cout << *i << ' ';

    return 0;
}
