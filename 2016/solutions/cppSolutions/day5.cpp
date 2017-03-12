//
// Created by Jarek Wojciechowski on 3/11/17.
//
#include <iostream>
#include "md5.h"


class password_generator{
    int hashingIndex = 0;
    std::string door_id;
    std::string pt1_generated_password = "";
    std::string pt2_generated_password = "        ";

    std::string generate_next_hash(){
        return md5(door_id + std::to_string(hashingIndex++));
    }

    bool hash_is_interesting(std::string hash){
        return hash.substr(0,5) == "00000";
    }

    bool pt2_not_complete(){
        return pt2_generated_password.find(" ") != std::string::npos;
    };

public:
    password_generator(std::string door_id){
        this->door_id = door_id;
    }
    void generate_final_passwords(){
        while (pt2_not_complete()){
            std::string next_hash = generate_next_hash();
            if(hash_is_interesting(next_hash)){
                std::cout << "Next interesting character is: " << next_hash[5] << "\n";
                if(pt1_generated_password.length() < 8) {
                    pt1_generated_password += next_hash[5];
                }
                int index = next_hash[5] - '0';
                if(index >= 0 && index < 10 && pt2_generated_password[index] == ' '){
                    pt2_generated_password[index] = next_hash[6];
                }
            }
        }
    }
    std::string get_pt1_password(){return pt1_generated_password;};
    std::string get_pt2_password(){return pt2_generated_password;};
};


int solve_day5(){
    password_generator generator = password_generator("ojvtpuvg");
    generator.generate_final_passwords();
    std::cout << "Part 1 generated password: " << generator.get_pt1_password() << "\n";
    std::cout << "Part 2 generated password: " << generator.get_pt2_password();
}
