//
// Created by Jarek Wojciechowski on 3/8/17.
//

class Keypad{
    std::pair<int,int> xy_location;
    int keypad_grid[5][5];
    std::vector<char> final_input;

public:
    Keypad(){
        keypad_grid ={{0,0,0,0,0},
                      {0,1,2,3,0},
                      {0,4,5,6,0},
                      {0,7,8,9,0},
                      {0,0,0,0,0}};
    }
    void move_on_keypad(char direction){
        //Get new movement location
        //Check if out of bounds
        //Move to location if within bounds

    }
    void finalize_keyboard_location(){ final_input.push_back(keypad_grid[xy_location.first][xy_location.second]); }
    string final_keypad_input(){
        //Probably need to concatenate this into a string
        return final_input;
    }

};


int solve_day2(){
    keypad = Keypad();
    //Get one line
    //Move based on each character
    //Finalize each character at the end of a line
    //Output final keypad solution

}
