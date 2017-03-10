//
// Created by Jarek Wojciechowski on 3/10/17.
//

#include <iostream>
#include <fstream>
#include <map>

class signal_processor{
    int character_counter[8][26] = { {0} };
public:
    signal_processor(){}
    void process_message(std::string new_message){
        //First dimension corresponds to each character position in the string
        //Second dimension corresponds to eahc letter in the alphabet
        for(int i=0; i < new_message.length(); i++){
            character_counter[i][new_message[i] - 'a']++;
        }
    }

    std::string get_max_final_message(){
        std::string output_string = "";
        for(int i=0; i < 8 /**Hardcoded because I don't know how to get the first length**/; i++){
            //for each character position, find the highest frequency, and get the index, then converts it back into a character
            output_string +=
                std::distance(character_counter[i], std::max_element(character_counter[i], character_counter[i] + 26)) + 'a';
        }
        return output_string;
    }
    std::string get_min_final_message(){
        std::string output_string = "";
        for(int i=0; i < 8 /**Hardcoded because I don't know how to get the first length**/; i++){
            //for each character position, find the highest frequency, and get the index, then converts it back into a character
            output_string +=
                    std::distance(character_counter[i], std::min_element(character_counter[i], character_counter[i] + 26)) + 'a';
        }
        return output_string;
    }
};

int solve_day6(){
    FILE *fp;
    if ((fp = fopen("day6input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }
    signal_processor sig_processor = signal_processor();
    char temp_cstr[9];
    std::string message;

    while (fscanf(fp, "%s", &temp_cstr) > 0) {
        message = temp_cstr;
        sig_processor.process_message(message);
    }

    std::cout << "Max-rep cipher message: " << sig_processor.get_max_final_message() << "\n";
    std::cout << "Min-rep cipher message: " << sig_processor.get_min_final_message();
}
