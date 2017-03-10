//
// Created by Jarek Wojciechowski on 3/10/17.
//

#include <iostream>
#include <fstream>
#include <map>

class signal_processor{
    std::map<char, int> character_counter[8];
public:
    signal_processor(){}
    void process_message(std::string new_message){
        for(int i=0; i < new_message.length(); i++){
            character_counter[new_message[i]]++;
        }
    }
};

int solve_day3(){
    FILE *fp;
    if ((fp = fopen("day6input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }
    signal_processor sig_processor = signal_processor();
    std::string message;

    while (fscanf(fp, "", &message) == 1) {
       sig_processor.process_message(message);
    }

}
